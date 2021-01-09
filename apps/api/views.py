from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .authenticated import CustomAuthenticated
from .serializers import (CountrySerializer, ArtistSerializer, AlbumSerializer,
                          SongsSerializer)
from apps.countries.models import Countries
from apps.artists.models import Artists
from apps.albums.models import Albums
from apps.songs.models import Songs


class CountryApiView(APIView):
    permission_classes = [CustomAuthenticated]

    def get(self, request, name=None):
        if name is not None:
            countries = Countries.objects.get(name=name)
            serializer = CountrySerializer(countries)
        else:
            countries = Countries.objects.all()
            serializer = CountrySerializer(countries, many=True)
        return Response({'países': serializer.data})

    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            country = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name=None):
        return Response({'m': 'pu'})

    def delete(self, request, name=None):
        country = get_object_or_404(Countries.objects.all(), name=name)
        country.delete()
        return Response({'message': 'País eliminado'},
                        status=status.HTTP_200_OK)


class ArtistApiView(APIView):
    permission_classes = [CustomAuthenticated]

    def get(self, request, name=None):
        if name is not None:
            artist = get_object_or_404(Artists.objects.all(), name=name)
            serializer = ArtistSerializer(artist)
            return Response({'artista': serializer.data})
        else:
            artists = Artists.objects.all()
            serializer = ArtistSerializer(artists, many=True)
            return Response({'artistas': serializer.data})

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            artist = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name=None):
        artist = get_object_or_404(Artists.objects.all(), name=name)
        serializer = ArtistSerializer(instance=artist, data=request.data,
                                      partial=True)
        if serializer.is_valid(raise_exception=True):
            artist = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

    def delete(self, request, name=None):
        artist = get_object_or_404(Artists.objects.all(), name=name)
        name = artist.name
        artist.delete()
        return Response({'message': f'Artista {name} eliminado'},
                        status=status.HTTP_200_OK)


class AlbumApiView(APIView):
    permission_classes = [CustomAuthenticated]

    def get(self, request, name=None):
        if name is not None:
            album = get_object_or_404(Albums.objects.all(), name=name)
            serializer = AlbumSerializer(album)
            return Response({'album': serializer.data})
        else:
            albums = Albums.objects.all()
            serializer = AlbumSerializer(albums, many=True)
            return Response({'albums': serializer.data})

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            album = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name=None):
        album = get_object_or_404(Albums.objects.all(), name=name)
        serializer = AlbumSerializer(instance=album, data=request.data,
                                      partial=True)
        if serializer.is_valid(raise_exception=True):
            artist = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

    def delete(self, request, name=None):
        album = get_object_or_404(Albums.objects.all(), name=name)
        name = album.name
        album.delete()
        return Response({'message': f'Album {name} eliminado'},
                        status=status.HTTP_200_OK)


class SongApiView(APIView):
    permission_classes = [CustomAuthenticated]

    def get(self, request, name=None):
        if name is not None:
            song = get_object_or_404(Songs.objects.all(), name=name)
            serializer = SongsSerializer(song)
            return Response({'cancion': serializer.data})
        else:
            songs = Songs.objects.all()
            serializer = SongsSerializer(songs, many=True)
            return Response({'canciones': serializer.data})

    def post(self, request):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            song = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name=None):
        song = get_object_or_404(Songs.objects.all(), name=name)
        serializer = SongsSerializer(instance=song, data=request.data,
                                     partial=True)
        if serializer.is_valid(raise_exception=True):
            song = serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

    def delete(self, request, name=None):
        song = get_object_or_404(Songs.objects.all(), name=name)
        name = song.name
        song.delete()
        return Response({'message': f'Canción {name} eliminada'},
                        status=status.HTTP_200_OK)


class SongsListByAlbum(APIView):
    """
    Lista de conciones por album
    """
    def get(self, request, name=None):
        album = Albums.objects.get(name=name)
        serializer = SongsSerializer(album.songs_set, many=True)
        return Response(serializer.data)


class SongsListByArtist(APIView):
    """
    Lista de conciones por artista
    """
    def get(self, request, name=None):
        artist = Artists.objects.get(name=name)
        songs = []
        for album in artist.albums_set.all():
            for song in album.songs_set.all():
                songs.append(song)
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)


class AlbumsListByArtist(APIView):
    """
    Lista de albums por artista
    """
    def get(self, request, name=None):
        artist = Artists.objects.get(name=name)
        serializer = AlbumSerializer(artist.albums_set, many=True)
        return Response(serializer.data)

