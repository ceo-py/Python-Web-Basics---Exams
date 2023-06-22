from django.shortcuts import render

from apps.functionality.items import get_all_items
from apps.recipes.models import RecipesModel


# Create your views here.
def index(request):

    return render(request, 'common/index.html', context={
        'recipes': get_all_items(RecipesModel)
    })
