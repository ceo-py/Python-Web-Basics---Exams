from django.shortcuts import render, redirect

from apps.autht.models import ProfileModel
from apps.functionality.items import get_all_items
from apps.functionality.profile import get_profile
from apps.note.models import NoteModel


# Create your views here.


def profile(request):

    context = {'profile': get_profile(ProfileModel),
               'notes': len(get_all_items(NoteModel))}
    return render(request, 'autht/profile.html', context)


def delete_profile(request):
    ProfileModel.objects.all().delete()
    NoteModel.objects.all().delete()

    return redirect('index')
