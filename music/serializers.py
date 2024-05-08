from rest_framework import serializers
from music.models import Artist, Album, Tracks


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = '__all__'


class SongsSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)

    class Meta:
        model = Tracks
        fields = '__all__'
