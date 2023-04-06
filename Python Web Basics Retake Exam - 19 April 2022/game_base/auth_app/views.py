from django.shortcuts import render

from game_base.auth_app.forms import (
    ProfileCreateForm,
    ProfileModelBaseForm,
    ProfileDeleteForm,
)
from game_base.auth_app.models import ProfileModel
from game_base.common_app.views import get_profile
from game_base.functionality.view_form import view_form
from game_base.game_app.models import GameModel


def get_names(item):
    return (" ").join(x for x in list(item.__dict__.values())[5:-1] if x is not None)


def create_profile(request):
    return view_form(
        request=request, base_form=ProfileCreateForm, redirect_url="index", base_url="auth_app/create-profile.html"
    )


def profile_details(request):
    all_games = sorted(GameModel.objects.all(), key=lambda x: x.pk)
    avr_rating = (
        sum(x.__dict__["rating"] for x in all_games) / len(all_games)
        if all_games
        else 0.0
    )
    context = {
        "profile": get_profile(ProfileModel),
        "name": get_names(get_profile(ProfileModel)),
        "games_counter": len(all_games),
        "avr_rating": avr_rating,
    }
    return render(request, "auth_app/details-profile.html", context)


def profile_edit(request):
    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        item_instance=get_profile(ProfileModel),
        redirect_url="profile_details",
        base_url="auth_app/edit-profile.html",
        addition_data={"profile": get_profile(ProfileModel)},
    )


def profile_delete(request):
    GameModel.objects.all().delete()
    return view_form(
        request=request,
        base_form=ProfileDeleteForm,
        item_instance=get_profile(ProfileModel),
        redirect_url="index",
        base_url="auth_app/delete-profile.html",
        addition_data=
        {"profile": get_profile(ProfileModel)},
        delete_form=True,
    )
