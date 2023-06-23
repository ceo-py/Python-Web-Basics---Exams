from django.shortcuts import render

from apps.functionality.items import get_all_items
from apps.functionality.user_profile import get_profile
from apps.functionality.view_form import view_form
from apps.game.models import GameModel
from apps.user_profile.forms import ProfileModelBaseForm
from apps.user_profile.models import ProfileModel


# Create your views here.

def index(request):
    profile = get_profile(ProfileModel)

    if profile:
        return view_form(
            request=request,
            base_form=ProfileModelBaseForm,
            redirect_url='index',
            base_url='common/home-page.html',
            addition_data={
            }
        )

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        redirect_url='index',
        base_url='common/home-page.html',
        addition_data={
            'no_profile': True
        }
    )


def dashboard(request):
    profile = get_profile(ProfileModel)
    if not profile:
        return view_form(
            request=request,
            base_form=ProfileModelBaseForm,
            redirect_url='index',
            base_url='common/home-page.html',
            addition_data={
                'no_profile': True
            }
        )

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        redirect_url='index',
        base_url='common/dashboard.html',
        addition_data={
            'games' : get_all_items(GameModel)
        }
    )
