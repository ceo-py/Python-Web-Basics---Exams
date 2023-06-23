from django.urls import path, include

from base.music_app.views import (
    index,
    album_add,
    album_details,
    album_edit,
    album_delete,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "album/",
        include(
            [
                path("add/", album_add, name="album_add"),
                path("details/<int:pk>/", album_details, name="album_details"),
                path("edit/<int:pk>/", album_edit, name="album_edit"),
                path("delete/<int:pk>/", album_delete, name="album_delete"),
            ]
        ),
    ),
]
