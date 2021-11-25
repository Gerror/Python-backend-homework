from django.db import models
from django.urls import reverse
from genres.models import Genre
from users.models import User
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название видео')
    description = models.TextField(verbose_name='Описание видео')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    year = models.IntegerField(verbose_name='Год', default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video_detail', kwargs={'video_id': self.id})

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
