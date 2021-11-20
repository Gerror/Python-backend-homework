from django.contrib import admin
from videos.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year')
    list_filter = ('year', 'genres')
    search_fields = ['title']
    ordering = ['year']


admin.site.register(Video, VideoAdmin)
