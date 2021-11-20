from django.contrib import admin
from genres.models import Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Genre, GenreAdmin)
