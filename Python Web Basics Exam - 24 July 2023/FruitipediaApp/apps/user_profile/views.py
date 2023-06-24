from django.shortcuts import render, redirect

from apps.fruits.models import FruitsModel
from apps.functionality.get_profile import get_profile
from apps.functionality.items import get_all_items
from apps.functionality.profile_exist import check_profile_exists
from apps.functionality.view_form import view_form
from apps.user_profile.forms import (
    ProfileCreateForm,
    ProfilesModelBaseForm,
    ProfileEditForm,
)
from apps.user_profile.models import ProfileModel


# Create your views here.


def profile_create(request):
    profile = get_profile(ProfileModel)

    if profile:
        return redirect("index")

    return view_form(
        request=request,
        base_form=ProfileCreateForm,
        redirect_url="dashboard",
        base_url="user_profile/create-profile.html",
        addition_data={"no_profile": True},
    )


@check_profile_exists
def profile_details(request):
    context = {
        "profile": get_profile(ProfileModel),
        "fruits": len(get_all_items(FruitsModel)),
    }
    return render(request, "user_profile/details-profile.html", context=context)


@check_profile_exists
def profile_edit(request):
    profile = get_profile(ProfileModel)
    return view_form(
        request=request,
        base_form=ProfileEditForm,
        item_instance=profile,
        redirect_url="profile_details",
        base_url="user_profile/edit-profile.html",
        addition_data={"profile": profile},
    )


@check_profile_exists
def profile_delete(request):
    if request.method == "POST":
        ProfileModel.objects.all().delete()
        FruitsModel.objects.all().delete()
        return redirect("index")

    return render(request, "user_profile/delete-profile.html")
