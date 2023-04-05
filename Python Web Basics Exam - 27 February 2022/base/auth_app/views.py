from django.shortcuts import render, redirect

from base.auth_app.forms import ProfileModelForm, ProfileDeleteForm
from base.auth_app.models import ProfileModel
from base.music_app.forms import AlbumDeleteForm
from base.music_app.models import AlbumModel


def delete_all_albums(albums):
    for album in albums:
        form = AlbumDeleteForm(instance=album)
        form.save()


def get_profile():
    return ProfileModel.objects.all()


def profile_details(request):
    context = {
        "profile": list(get_profile())[-1],
        "albums_counter": len(AlbumModel.objects.all()),
    }

    return render(request, "auth_app/profile-details.html", context)


def profile_delete(request):
    context = {"profile": list(get_profile())[-1]}

    if request.method == "POST":
        form = ProfileDeleteForm(instance=context["profile"])
        form.save()
        delete_all_albums(AlbumModel.objects.all())
        return redirect("index")

    return render(request, "auth_app/profile-delete.html", context)
