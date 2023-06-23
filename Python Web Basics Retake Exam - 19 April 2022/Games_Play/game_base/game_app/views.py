from django.shortcuts import render

from game_base.auth_app.models import ProfileModel
from game_base.functionality.items import get_all_items, find_item
from game_base.functionality.profile import get_profile
from game_base.functionality.view_form import view_form
from game_base.game_app.forms import GameModelBaseForm, GameDeleteForm
from game_base.game_app.models import GameModel


def dashboard(request):
    context = {'games': get_all_items(GameModel),
               'profile': get_profile(ProfileModel)
               }
    return render(request, r'game_app\dashboard.html', context)


def game_create(request):
    return view_form(
        request=request,
        base_form=GameModelBaseForm,
        redirect_url='dashboard',
        base_url='game_app/create-game.html',
        addition_data={'profile': get_profile(ProfileModel)}
    )


def game_details(request, pk):
    context = {
        'game': find_item(GameModel, pk),
        'profile': get_profile(ProfileModel)
    }

    return render(request, r'game_app\details-game.html', context)


def game_edit(request, pk):
    game = find_item(GameModel, pk)
    return view_form(
        request=request,
        base_form=GameModelBaseForm,
        item_instance=game,
        redirect_url='dashboard',
        base_url=r'game_app\edit-game.html',
        addition_data={'game': game,
                       'profile': get_profile(ProfileModel)})


def game_delete(request, pk):
    game = find_item(GameModel, pk)
    return view_form(
        request=request,
        base_form=GameDeleteForm,
        item_instance=game,
        redirect_url='dashboard',
        base_url=r'game_app\delete-game.html',
        addition_data={'game': game,
                       'profile': get_profile(ProfileModel)},
        delete_form=True)
