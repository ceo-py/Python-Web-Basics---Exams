from django.shortcuts import render

from apps.functionality.items import find_item
from apps.functionality.view_form import view_form
from apps.game.forms import GameModelBaseForm, GameModelDeleteForm
from apps.game.models import GameModel


# Create your views here.

def game_create(request):
    return view_form(
        request=request,
        base_form=GameModelBaseForm,
        redirect_url='dashboard',
        base_url='game/create-game.html',
    )


def game_details(request, pk):
    game = find_item(GameModel, pk)
    return view_form(
        request=request,
        item_instance=game,
        base_form=GameModelBaseForm,
        redirect_url='dashboard',
        base_url='game/details-game.html',
        addition_data={
            'game': game
        }
    )


def game_edit(request, pk):
    game = find_item(GameModel, pk)
    return view_form(
        request=request,
        item_instance=game,
        base_form=GameModelBaseForm,
        redirect_url='dashboard',
        base_url='game/edit-game.html',
        addition_data={
            'game': game
        }
    )


def game_delete(request, pk):
    game = find_item(GameModel, pk)
    return view_form(
        request=request,
        item_instance=game,
        base_form=GameModelDeleteForm,
        redirect_url='dashboard',
        base_url='game/delete-game.html',
        addition_data={
            'game': game
        },
        delete_form=True
    )
