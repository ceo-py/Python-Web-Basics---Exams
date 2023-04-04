from django.shortcuts import render, redirect

from base.auth_app.views import get_profile, get_context_profile
from base.game_app.forms import GameModelBaseForm, GameDeleteForm
from base.game_app.models import GameModel


def get_all_games():
    return GameModel.objects.all()


def home_page(request):
    context = get_context_profile(get_profile())
    return render(request, 'home-page.html', context)


def dashboard(request):
    context = get_context_profile(get_profile())
    context['games'] = sorted(get_all_games(), key=lambda x: x.pk)

    return render(request, 'dashboard.html', context)


def game_create(request):
    context = get_context_profile(get_profile())

    if request.method == 'GET':
        form = GameModelBaseForm()
    else:
        form = GameModelBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context['form'] = form

    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    context = get_context_profile(get_profile())
    context['game'] = GameModel.objects.filter(pk=pk).get()

    return render(request, 'game/details-game.html', context)


def game_edit(request, pk):
    context = get_context_profile(get_profile())
    context['game'] = GameModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameModelBaseForm(instance=context['game'])
    else:
        form = GameModelBaseForm(request.POST, instance=context['game'])
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context['form'] = form
    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    context = get_context_profile(get_profile())
    context['game'] = GameModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameDeleteForm(instance=context['game'])
    else:
        form = GameDeleteForm(request.POST, instance=context['game'])
        form.save()
        return redirect('dashboard')

    context['form'] = form

    return render(request, 'game/delete-game.html', context)