from django.db import models
from genres.models import Genre

class Video(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название видео')
    description = models.TextField(verbose_name='Описание видео')
    genres = models.ManyToManyField(Genre)
