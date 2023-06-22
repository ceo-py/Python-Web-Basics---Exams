from django.shortcuts import render, redirect

from apps.functionality.get_profile import get_profile
from apps.functionality.items import get_all_items
from apps.notes.models import NotesModel
from apps.user_profile.models import ProfileModel


# Create your views here.
def profile_details(request):

    context = {'profile': get_profile(ProfileModel),
               'total_notes': len(get_all_items(NotesModel))}

    return render(request, 'user_profile/profile.html', context)


def profile_delete(request):
    NotesModel.objects.all().delete()
    ProfileModel.objects.all().delete()
    return redirect('index')

