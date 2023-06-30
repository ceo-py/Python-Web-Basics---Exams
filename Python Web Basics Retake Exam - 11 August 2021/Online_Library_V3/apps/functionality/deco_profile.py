from django.http import HttpResponse
from django.shortcuts import render

from apps.books.models import BooksModel
from apps.functionality.get_profile import get_profile
from apps.functionality.items import get_all_items
from apps.functionality.view_form import view_form
from apps.user_profile.forms import ProfileCreateForm
from apps.user_profile.models import ProfileModel


def check_profile_exists(view_func):
    def wrapper(request, *args, **kwargs):
        profile = get_profile(ProfileModel)
        if not profile:
            return view_form(
                request=request,
                base_form=ProfileCreateForm,
                item_instance=profile,
                redirect_url='index',
                base_url='common/home-no-profile.html',
                addition_data={
                    'profile': profile
                }
            )

        response = view_func(request, *args, **kwargs)

        if not isinstance(response, HttpResponse):
            return render(request, 'common/home-with-profile.html', context={
                'profile': profile,
                'books': get_all_items(BooksModel)
            })

        return response

    return wrapper
