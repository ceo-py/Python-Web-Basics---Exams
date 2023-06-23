from django.shortcuts import render, redirect

from apps.functionality.get_profile import get_profile
from apps.functionality.items import get_all_items
from apps.functionality.profile_exist import check_profile_exists
from apps.functionality.view_form import view_form
from apps.plants.models import PlantsModel
from apps.user_profile.forms import ProfileCreateForm, ProfilesModelBaseForm
from apps.user_profile.models import ProfileModel


# Create your views here.

def profile_create(request):
    return view_form(
        request=request,
        base_form=ProfileCreateForm,
        redirect_url='index',
        base_url='user_profile/create-profile.html',
        addition_data={
            'no_profile': True
        }
    )


@check_profile_exists
def profile_details(request):
    context = {
        'profile': get_profile(ProfileModel),
        'plants': len(get_all_items(PlantsModel))
    }
    return render(request, 'user_profile/profile-details.html', context=context)


@check_profile_exists
def profile_edit(request):
    profile = get_profile(ProfileModel)
    return view_form(
        request=request,
        base_form=ProfilesModelBaseForm,
        item_instance=profile,
        redirect_url='catalogue',
        base_url='user_profile/edit-profile.html',
        addition_data={
            'profile': profile
        }
    )


@check_profile_exists
def profile_delete(request):
    if request.method == 'POST':
        ProfileModel.objects.all().delete()
        PlantsModel.objects.all().delete()
        return redirect('index')

    return render(request, 'user_profile/delete-profile.html')
