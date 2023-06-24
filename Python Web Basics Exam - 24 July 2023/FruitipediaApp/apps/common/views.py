from django.shortcuts import render

from apps.fruits.models import FruitsModel
from apps.functionality.items import get_all_items
from apps.functionality.profile_exist import check_profile_exists


# Create your views here.
@check_profile_exists
def index(request):
    return render(request, "common/index.html")


@check_profile_exists
def dashboard(request):
    return render(
        request, "common/dashboard.html", {"fruits": get_all_items(FruitsModel)}
    )
