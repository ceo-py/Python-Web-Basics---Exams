from django.shortcuts import render, redirect

from base.auth_app.forms import ProfileCreateModel, ProfileModelBaseModel, ProfileDeleteModel
from base.auth_app.models import ProfileModel
from base.game_app.models import GameModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def get_context_profile(profile):
    return {
        'profile': profile
    }


def get_profile_name(profile):

    return (' ').join(
        [
            name for name in list(get_profile().__dict__.values())[5:-1] if name is not None
        ]
    )


def profile_create(request):
    context = get_context_profile(get_profile())

    if context['profile']:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateModel()

    else:
        form = ProfileCreateModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context['form'] = form

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    context = get_context_profile(get_profile())
    context['name'] = get_profile_name(get_profile())
    games = GameModel.objects.all()
    context['total_games'] = len(games)
    context['avr_rating'] = sum(game.rating for game in games)/context['total_games'] if context['total_games'] else 0.00

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    context = get_context_profile(get_profile())

    if request.method == 'GET':
        form = ProfileModelBaseModel(instance=context['profile'])
    else:
        form = ProfileModelBaseModel(request.POST, instance=context['profile'])
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context['form'] = form

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    context = get_context_profile(get_profile())

    if request.method == 'POST':
        form = ProfileDeleteModel(request.POST, instance=context['profile'])
        form.save()
        return redirect('index')

    return render(request, 'profile/delete-profile.html', context)

