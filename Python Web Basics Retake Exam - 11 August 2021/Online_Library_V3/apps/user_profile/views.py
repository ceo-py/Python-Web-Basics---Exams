from django.shortcuts import render, redirect

from apps.books.models import BooksModel
from apps.functionality.deco_profile import check_profile_exists
from apps.functionality.get_profile import get_profile
from apps.functionality.view_form import view_form
from apps.user_profile.forms import ProfileModelBaseForm, ProfileDeleteForm
from apps.user_profile.models import ProfileModel


# Create your views here.
@check_profile_exists
def profile_details(request):
    profile = get_profile(ProfileModel)

    return render(request, 'user_profile/profile.html', context={
        'profile': profile
    })


@check_profile_exists
def profile_edit(request):
    profile = get_profile(ProfileModel)

    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        item_instance=profile,
        redirect_url='index',
        base_url='user_profile/edit-profile.html',
        addition_data={
            'profile': profile,
        }
    )


@check_profile_exists
def profile_delete(request):
    profile = get_profile(ProfileModel)

    if request.method == "POST":
        ProfileModel.objects.all().delete()
        BooksModel.objects.all().delete()
        return redirect('index')

    return view_form(
        request=request,
        base_form=ProfileDeleteForm,
        item_instance=profile,
        redirect_url='index',
        base_url='user_profile/delete-profile.html',
        addition_data={
            'profile': profile,
        }
    )
