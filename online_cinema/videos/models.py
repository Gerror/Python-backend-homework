from django.db import models
from django.urls import reverse
from genres.models import Genre

class Video(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name='Название видео')
    description = models.TextField(verbose_name='Описание видео')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    year = models.IntegerField(verbose_name='Год', default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={'video_id': self.id})

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
