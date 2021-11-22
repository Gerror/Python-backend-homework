from videos.models import Video
from rest_framework import serializers
from genres.serializers import GenreSerializer
from genres.models import Genre


class VideoSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, required=False)

    def create_or_update(self, validated_data, video=None):
        if not video:
            video = Video()
        if validated_data.get('title'):
            video.title = validated_data.get('title')
        if validated_data.get('description'):
            video.description = validated_data.get('description')
        if validated_data.get('year'):
            video.year = validated_data.get('year')

        video.save()

        if validated_data.get('genres'):
            video.genres.set([])
            for serialized_genre in validated_data.get('genres'):
                genre = Genre.objects.get(title=serialized_genre['title'])
                video.genres.add(genre)

        return video

    def create(self, validated_data):
        return self.create_or_update(validated_data)

    def update(self, instance, validated_data):
        return self.create_or_update(validated_data, instance)

    def validate_genres(self, value):
        for serialized_genre in value:
            try:
                Genre.objects.get(title=serialized_genre['title'])
            except Genre.DoesNotExist as error:
                raise serializers.ValidationError(error)
        return value

    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'year', 'genres']
        read_only_fields = ['id']
