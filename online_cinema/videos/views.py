from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseNotAllowed
import json

def create_video(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"], "405 Method not allowed")

    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)

    result = {
        "status": "ok",
        "id": 123,
    }
    result.update(body)

    return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

def video_list(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"], "405 Method not allowed")

    return JsonResponse({
        "videos": [
            {
                "video_id": 123,
                "title": "Гарри Поттер и философский камень",
                "year": 2001
            },
            {
                "video_id": 321,
                "title": "Гарри Поттер и Тайная комната",
                "year": 2002
            },
            {
                "video_id": 213,
                "title": "Гарри Поттер и узник Азкабана",
                "year": 2004
            }
        ]
    }, json_dumps_params={"ensure_ascii": False})

def video_detail(request, video_id):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"], "405 Method not allowed")

    return JsonResponse(
        {
            "video_id": video_id,
            "title": "Гарри Поттер и философский камень",
            "description": "Гарри поступает в школу магии Хогвартс и заводит друзей. Первая часть большой франшизы о маленьком волшебнике",
            "year": 2001,
            "countries": [
                "Великобритания",
                "США"
            ],
            "genres": [
                "фэнтези",
                "приключения",
                "семейный"
            ]
        }, json_dumps_params={"ensure_ascii": False})
