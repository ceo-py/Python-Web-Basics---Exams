from django.shortcuts import render, redirect

from base.auth_app.forms import ProfileModelForm
from base.auth_app.views import get_profile
from base.music_app.forms import AlbumModelBaseForm, AlbumDeleteForm
from base.music_app.models import AlbumModel


def get_albums():
    return AlbumModel.objects.all().order_by('pk')


def find_album(pk):
    return AlbumModel.objects.filter(pk=pk).get()


def index(request):
    context = {"profile": get_profile()}
    if context["profile"]:
        return index_with_profile(request, context)

    return index_no_profile(request, context)


def index_with_profile(request, context):
    context["albums"] = get_albums()
    return render(request, "music_app/home-with-profile.html", context)


def index_no_profile(request, context):

    if request.method == "GET":
        form = ProfileModelForm()
    else:
        form = ProfileModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context["form"] = form

    return render(request, "music_app/home-no-profile.html", context)


def album_add(request):

    if request.method == "GET":
        form = AlbumModelBaseForm()

    else:
        form = AlbumModelBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {"form": form}

    return render(request, "music_app/add-album.html", context)


def album_details(request, pk):
    context = {"album": find_album(pk)}

    return render(request, "music_app/album-details.html", context)


def album_edit(request, pk):
    context = {"album": find_album(pk)}

    if request.method == "GET":
        form = AlbumModelBaseForm(instance=context["album"])
    else:
        form = AlbumModelBaseForm(request.POST, instance=context["album"])
        if form.is_valid():
            form.save()
            return redirect("index")

    context["form"] = form
    return render(request, "music_app/edit-album.html", context)


def album_delete(request, pk):
    context = {"album": find_album(pk)}

    if request.method == "GET":
        form = AlbumDeleteForm(instance=context["album"])
    else:
        form = AlbumDeleteForm(request.POST, instance=context["album"])
        form.save()
        return redirect("index")

    context["form"] = form

    return render(request, "music_app/delete-album.html", context)
