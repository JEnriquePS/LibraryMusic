import time

from rest_framework import serializers

from apps.countries.models import Countries
from apps.artists.models import Artists
from apps.albums.models import Albums
from apps.songs.models import Songs


class CountrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    def create(self, validated_data):
        instance = Countries()
        instance.name = validated_data.get('name')
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AlbumStringField(serializers.RelatedField):
    def to_representation(self, value):
        return '{} ({})'.format(value.name, value.year)


class ArtistSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    about = serializers.CharField()
    country = serializers.CharField()
    albums_set = AlbumStringField(many=True, read_only=True)

    def create(self, validated_data):
        instance = Artists()
        instance.name = validated_data.get('name')
        instance.about = validated_data.get('about')
        instance.country = Countries.objects.get(
            name=validated_data.get('country'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about',
                                                  instance.about)
        instance.country = Countries.objects.get(
            name=validated_data.get('country')
        )
        instance.save()
        return instance


class SongStringField(serializers.RelatedField):
    def to_representation(self, value):
        duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return '{} ({})'.format(value.name, duration)


class AlbumSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()
    year = serializers.DateField()
    artist = serializers.CharField()
    songs_set = SongStringField(many=True, read_only=True)
    duration = serializers.SerializerMethodField()

    def get_duration(self, obj):
        duration = 0
        for song in obj.songs_set.all():
            duration += song.duration
        return time.strftime('%H:%M:%S', time.gmtime(duration))

    def create(self, validated_data):
        instance = Albums()
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.year = validated_data.get('year')
        instance.artist = Artists.objects.get(
            name=validated_data.get('artist'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.year = validated_data.get('year', instance.year)
        instance.artist = Artists.objects.get(name=validated_data.get('artist', instance.artist.name))
        instance.save()
        return instance


class FormatDurationStringField(serializers.RelatedField):
    def to_representation(self, value):
        duration = time.strftime('%M:%S', time.gmtime(value.duration))
        return '{}'.format(duration)


class SongsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    duration = serializers.IntegerField()
    format_duration = serializers.SerializerMethodField()
    album = serializers.CharField()

    def get_format_duration(self, obj):
        return time.strftime('%M:%S', time.gmtime(obj.duration))

    def create(self, validated_data):
        instance = Songs()
        instance.name = validated_data.get('name')
        instance.duration = validated_data.get('duration')
        instance.album = Albums.objects.get(
            name=validated_data.get('album'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.duration = validated_data.get('duration',
                                                  instance.duration)
        instance.album = Albums.objects.get(
            name=validated_data.get('album'))
        instance.save()
        return instance
