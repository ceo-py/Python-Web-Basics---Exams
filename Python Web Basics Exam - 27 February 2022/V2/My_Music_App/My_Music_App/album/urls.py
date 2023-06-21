
from django.urls import path

from My_Music_App.album.views import album_add, album_details, album_edit, album_delete
from My_Music_App.common.views import index

urlpatterns = [
    path("add/", album_add, name='album_add'),
    path("details/<int:pk>/", album_details, name='album_details'),
    path("edit/<int:pk>/", album_edit, name='album_edit'),
    path("delete/<int:pk>/", album_delete, name='album_delete'),
]
