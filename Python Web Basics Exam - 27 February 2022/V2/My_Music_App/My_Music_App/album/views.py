from django.shortcuts import render

from My_Music_App.album.forms import AlbumModelBaseForm, AlbumModelDelete
from My_Music_App.album.models import Album
from My_Music_App.functionality.items import get_all_items, find_item
from My_Music_App.functionality.view_form import view_form


# Create your views here.


def album_add(request):
    return view_form(
        request=request,
        base_form=AlbumModelBaseForm,
        redirect_url='index',
        base_url='album/add-album.html',
    )


def album_details(request, pk):
    context = {"album": find_item(Album, pk)}

    return render(request, "album/album-details.html", context)


def album_edit(request, pk):
    album = find_item(Album, pk)
    return view_form(
        request=request,
        base_form=AlbumModelBaseForm,
        item_instance=album,
        redirect_url='index',
        base_url='album/edit-album.html',
        addition_data={
            'album': album}
    )


def album_delete(request, pk):
    album = find_item(Album, pk)

    return view_form(
        request=request,
        base_form=AlbumModelDelete,
        item_instance=album,
        redirect_url='index',
        base_url='album/delete-album.html',
        addition_data={'albums': get_all_items(Album),
                       'album': album
                       },
        delete_form=True)
