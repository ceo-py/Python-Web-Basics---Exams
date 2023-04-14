from django.shortcuts import render

from apps.autht.forms import ProfileModelBaseForm
from apps.autht.models import ProfileModel
from apps.functionality.items import get_all_items
from apps.functionality.profile import get_profile
from apps.functionality.view_model import view_form
from apps.note.models import NoteModel


# Create your views here.


def index(request):
    profile = get_profile(ProfileModel)

    if profile:
        context = {'profile': profile,
                   'notes': get_all_items(NoteModel)}
        return render(request, 'common/home-with-profile.html', context)

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        redirect_url='index',
        base_url='common/home-no-profile.html',
    )

