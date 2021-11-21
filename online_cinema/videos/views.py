from django.http.response import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.db.utils import IntegrityError
from videos.models import Video
from genres.models import Genre
import json


def validate_body(function):
    def wrapper(request, *args, **kwars):
        body_unicode = request.body.decode("utf-8")
        try:
            body = json.loads(body_unicode)
        except json.decoder.JSONDecodeError as error:
            return HttpResponseBadRequest(error)

        if "title" not in body:
            return HttpResponseBadRequest("Поле 'title' обязательно")

        return function(request, body, *args, **kwars)
    return wrapper


def create_or_update_video(body, video=None):
    if not video:
        video = Video()
    video.title = body["title"]

    if "description" in body:
        video.description = body["description"]
    if "year" in body:
        video.year = body["year"]

    try:
        video.save()
    except (ValueError, IntegrityError) as error:
        return HttpResponseBadRequest(error)

    if "genres" in body and isinstance(body["genres"], list):
        video.genres.set([])
        for genre_title in body["genres"]:
            try:
                genre = Genre.objects.get(title=genre_title)
                video.genres.add(genre)
            except Genre.DoesNotExist:
                continue

    return JsonResponse({
        "status": "ok",
        "id": video.id
    }, json_dumps_params={"ensure_ascii": False})


def get_video_data(video):
    return {
            "id": video.id,
            "title": video.title,
            "description": video.description,
            "genres": [genre.title for genre in video.genres.all()]
           }


@require_POST
@validate_body
def create_video(request, body):
    return create_or_update_video(body)


@require_GET
def video_list(request):
    videos = Video.objects.all()
    data = [
        get_video_data(video) for video in videos
    ]
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False}, safe=False)


@require_GET
def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return JsonResponse(get_video_data(video), json_dumps_params={"ensure_ascii": False})


@require_http_methods(["PUT"])
@validate_body
def update_video(request, body, video_id):
    try:
        video = Video.objects.get(id=video_id)
    except Video.DoesNotExist:
        video = None
    finally:
        return create_or_update_video(body, video)


@require_http_methods(["DELETE"])
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    return JsonResponse({"status": "ok"}, json_dumps_params={"ensure_ascii": False})
