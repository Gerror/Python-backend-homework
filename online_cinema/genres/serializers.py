from genres.models import Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'title']
        read_only_fields = ['id']
        extra_kwargs = {
            'title': {'validators': []},
        }
