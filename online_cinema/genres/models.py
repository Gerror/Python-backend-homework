from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name='Название жанра')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'