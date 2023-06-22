from django.shortcuts import render

from apps.books.models import BookModel
from apps.functionality.get_profile import get_profile
from apps.functionality.items import get_all_items
from apps.functionality.view_form import view_form
from apps.user_profile.forms import ProfileModelBaseForm, ProfileDeleteForm
from apps.user_profile.models import ProfileModel


# Create your views here.
def profile_details(request):
    profile = get_profile(ProfileModel)

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        item_instance=profile,
        redirect_url='index',
        base_url='user_profile/profile.html',
        addition_data={
            'profile': profile
        }
    )


def profile_edit(request):
    profile = get_profile(ProfileModel)

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        item_instance=profile,
        redirect_url='index',
        base_url='user_profile/edit-profile.html',
        addition_data={
            'profile': profile
        }
    )


def profile_delete(request):
    profile = get_profile(ProfileModel)

    if request.method == 'POST':
        BookModel.objects.all().delete()

    return view_form(
        request=request,
        base_form=ProfileDeleteForm,
        item_instance=profile,
        redirect_url='index',
        base_url='user_profile/delete-profile.html',
        addition_data={
            'profile': profile},
        delete_form=True
    )
