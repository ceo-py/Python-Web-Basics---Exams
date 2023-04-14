from django.shortcuts import render, redirect

from apps.functionality.items import get_all_items
from apps.functionality.profile import get_profile
from apps.notes.models import NoteModel
from apps.user.models import ProfileModel


# Create your views here.


def user_profile(request):
    context = {'profile': get_profile(ProfileModel),
               'notes': len(get_all_items(NoteModel))}
    return render(request, 'user/profile.html', context)


def user_profile_delete(request):
    ProfileModel.objects.all().delete()
    NoteModel.objects.all().delete()
    return redirect('index')
