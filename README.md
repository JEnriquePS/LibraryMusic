# LibraryMusic
DRF API 

**API Restfull** con los metodos **CRUD** y autenticación para los metodos **POST**, **PUT** y **DELETE**

## Creación de entorno virtual
```bash
pyenv install 3.7.9
pyenv global 3.7.9
pyenv virtualenv LibraryMusic
pyenv activate LibraryMusic
```

## Instalar requerimientos de proyecto en entorno virtual:

```bash
pip install -r requirements/local.txt
```

## Configuracion de entorno de variables .env con:

```bash
SECRET_KEY="****************************************+"
DATABASE_URL="postgres://USER:PASSWORD@HOST:PORT/NAME"
```

## Ejecutar Proyecto:

```bash
python manage.py migrate
python manage.py runserver
```

El atributo **name** es utilizado para identicar el objeto en los querys, ya que es un campo unique.

```python
path('token/', TokenObtainPairView.as_view()),
path('token/update/', TokenRefreshView.as_view()),

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

path('album/full/songs/<str:name>/', SongsListByAlbum.as_view()),
path('artist/full/songs/<str:name>/', SongsListByArtist.as_view()),
path('artist/full/albums/<str:name>/', AlbumsListByArtist.as_view())
```
