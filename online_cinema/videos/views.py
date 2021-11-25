from rest_framework import viewsets
from videos.models import Video
from videos.serializers import VideoSerializer
from application.views import login_required


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @login_required
    def list(self, request):
        return super(VideoViewSet, self).list(request)

    @login_required
    def create(self, request):
        return super(VideoViewSet, self).create(request)

    @login_required
    def retrieve(self, request, pk=None):
        return super(VideoViewSet, self).retrieve(request, pk)

    @login_required
    def update(self, request, pk=None):
        return super(VideoViewSet, self).update(request, pk)

    @login_required
    def partial_update(self, request, pk=None):
        return super(VideoViewSet, self).partial_update(request, pk)

    @login_required
    def destroy(self, request, pk=None):
        return super(VideoViewSet, self).destroy(request, pk)
