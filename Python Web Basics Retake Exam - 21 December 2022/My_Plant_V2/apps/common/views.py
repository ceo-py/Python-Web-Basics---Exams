from django.shortcuts import render

from apps.functionality.items import get_all_items
from apps.functionality.profile_exist import check_profile_exists
from apps.plants.models import PlantsModel


# Create your views here.

@check_profile_exists
def index(request):
    pass


@check_profile_exists
def catalogue(request):
    return render(request, 'common/catalogue.html', {'plants': get_all_items(PlantsModel)})