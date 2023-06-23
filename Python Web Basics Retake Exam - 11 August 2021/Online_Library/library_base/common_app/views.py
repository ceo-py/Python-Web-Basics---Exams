from django.shortcuts import render

from library_base.auth_app.forms import ProfileModelBaseForm
from library_base.auth_app.models import ProfileModel
from library_base.book_app.models import BookModel
from library_base.functionality.items import get_all_items
from library_base.functionality.profile import get_profile
from library_base.functionality.view_form import view_form


def index(request):

    context = {'profile': get_profile(ProfileModel)}

    if context['profile']:
        context['books'] = get_all_items(BookModel)

        return render(request, 'common_app/home-with-profile.html', context)

    return view_form(
            request=request,
            base_form=ProfileModelBaseForm,
            redirect_url='index',
            base_url='common_app/home-no-profile.html',
            addition_data=context,
    )
