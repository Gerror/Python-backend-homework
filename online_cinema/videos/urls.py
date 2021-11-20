from django.contrib import admin
from django.urls import path
from videos.views import create_video, video_detail, video_list, delete_video, update_video

urlpatterns = [
    path('video/<int:video_id>/', video_detail, name="video_detail"),
    path('list/', video_list, name="video_list"),
    path('create/', create_video, name="create_video"),
    path('delete/<int:video_id>/', delete_video, name="delete_video"),
    path('update/', update_video, name="update_video")
]