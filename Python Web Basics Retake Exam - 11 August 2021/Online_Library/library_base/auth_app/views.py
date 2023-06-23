from django.shortcuts import render

from library_base.auth_app.forms import ProfileModelBaseForm, ProfileDeleteForm
from library_base.auth_app.models import ProfileModel
from library_base.book_app.models import BookModel
from library_base.functionality.profile import get_profile
from library_base.functionality.view_form import view_form


def profile(request):
    context = {
        'profile': get_profile(ProfileModel)
    }
    return render(request, 'auth_app/profile.html', context)


def profile_edit(request):
    profile = get_profile(ProfileModel)
    return view_form(
        request=request,
        base_form=ProfileModelBaseForm,
        item_instance=profile,
        redirect_url='profile',
        base_url='auth_app/edit-profile.html',
        addition_data={
            'profile': profile}
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
        base_url='auth_app/delete-profile.html',
        addition_data={
            'profile': profile},
        delete_form=True
    )
