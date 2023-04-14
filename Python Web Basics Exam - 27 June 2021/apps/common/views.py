from django.shortcuts import render

from apps.functionality.items import get_all_items
from apps.functionality.profile import get_profile
from apps.functionality.view_form import view_form
from apps.notes.models import NoteModel
from apps.user.forms import ProfileModelBaseForm
from apps.user.models import ProfileModel


# Create your views here.

def index(request):

    profile = get_profile(ProfileModel)

    if profile:
        contex = {'profile': profile,
                  'notes': get_all_items(NoteModel)}
        return render(request, 'common/home-with-profile.html', contex)

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        redirect_url='index',
        base_url='common/home-no-profile.html',
        addition_data={'profile': profile}
    )






