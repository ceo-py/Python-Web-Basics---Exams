from django.shortcuts import render, redirect

from My_Music_App.album.models import Album
from My_Music_App.functionality.items import get_all_items
from My_Music_App.user_profile.models import ProfileModel


# Create your views here.


def profile_details(request):
    context = {"profile": get_all_items(ProfileModel)[0],
               'albums_number': len(get_all_items(Album))}

    return render(request, "user_profile/profile-details.html", context)


def profile_delete(request):

    if request.method == "POST":
        ProfileModel.objects.all().delete()
        Album.objects.all().delete()
        return redirect('index')

    return render(request, "user_profile/profile-delete.html")
