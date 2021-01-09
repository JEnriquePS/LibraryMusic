from django.urls import path
from .views import *
urlpatterns = [
    path('country/create/', CountryApiView.as_view()),
    path('country/list/', CountryApiView.as_view()),
    path('country/detail/<str:name>/', CountryApiView.as_view()),
    path('country/update/<str:name>/', CountryApiView.as_view()),
    path('country/delete/<str:name>/', CountryApiView.as_view()),

    path('artist/create/', ArtistApiView.as_view()),
    path('artist/list/', ArtistApiView.as_view()),
    path('artist/detail/<str:name>/', ArtistApiView.as_view()),
    path('artist/update/<str:name>/', ArtistApiView.as_view()),
    path('artist/delete/<str:name>/', ArtistApiView.as_view()),

    path('album/create/', AlbumApiView.as_view()),
    path('album/list/', AlbumApiView.as_view()),
    path('album/detail/<str:name>/', AlbumApiView.as_view()),
    path('album/update/<str:name>/', AlbumApiView.as_view()),
    path('album/delete/<str:name>/', AlbumApiView.as_view()),

    path('song/create/', SongApiView.as_view()),
    path('song/list/', SongApiView.as_view()),
    path('song/detail/<str:name>/', SongApiView.as_view()),
    path('song/update/<str:name>/', SongApiView.as_view()),
    path('song/delete/<str:name>/', SongApiView.as_view()),


]