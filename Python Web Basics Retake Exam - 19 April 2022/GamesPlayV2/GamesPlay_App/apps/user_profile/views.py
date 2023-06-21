from django.shortcuts import render, redirect

from apps.functionality.items import get_all_items
from apps.functionality.view_form import view_form
from apps.game.models import GameModel
from apps.user_profile.forms import ProfileModelBaseForm, ProfileCreateForm
from apps.user_profile.models import ProfileModel


# Create your views here.

def profile_create(request):
    return view_form(
        request=request,
        base_form=ProfileCreateForm,
        redirect_url='index',
        base_url='user_profile/create-profile.html',
        addition_data={
        }
    )


def profile_details(request):
    profile = get_all_items(ProfileModel)[0]
    games = get_all_items(GameModel)
    total_games = len(games)
    name = f'{profile.first_name} {profile.last_name}'.replace('None', '')
    average_rating = sum(x.rating for x in games) / total_games if total_games > 0 else 0.0

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        redirect_url='index',
        base_url='user_profile/details-profile.html',
        addition_data={
            'profile': profile,
            'total_games': total_games,
            'average_rating': average_rating,
            'full_name': name
        }
    )


def profile_edit(request):
    profile = get_all_items(ProfileModel)[0]
    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        item_instance=profile,
        redirect_url='index',
        base_url='user_profile/edit-profile.html',
    )


def profile_delete(request):
    if request.method == "POST":
        ProfileModel.objects.all().delete()
        GameModel.objects.all().delete()
        return redirect('index')

    return render(request, "user_profile/delete-profile.html")