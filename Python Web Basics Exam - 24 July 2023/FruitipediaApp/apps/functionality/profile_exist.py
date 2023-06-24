from django.http import HttpResponse
from django.shortcuts import render

from apps.functionality.get_profile import get_profile
from apps.user_profile.models import ProfileModel


def check_profile_exists(view_func):
    def wrapper(request, *args, **kwargs):
        profile = get_profile(ProfileModel)
        if not profile:
            return render(request, "common/index.html", {"no_profile": True})

        response = view_func(request, *args, **kwargs)

        if not isinstance(response, HttpResponse):
            return render(request, "common/dashboard.html")

        return response

    return wrapper
