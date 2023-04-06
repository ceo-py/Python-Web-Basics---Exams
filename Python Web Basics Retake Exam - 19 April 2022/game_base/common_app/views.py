from django.shortcuts import render

from game_base.auth_app.models import ProfileModel
from game_base.functionality.profile import get_profile


def index(request):

    context = {
        'profile': get_profile(profile_model=ProfileModel)
    }

    return render(request, 'common_app/home-page.html', context)
