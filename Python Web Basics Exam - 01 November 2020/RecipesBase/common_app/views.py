from django.shortcuts import render

from RecipesBase.functionality.items import get_all_items
from RecipesBase.recipes_app.models import RecipeModel


def index(request):
    return render(request,
                  'common_app/index.html',
                  context={'recipes': get_all_items(RecipeModel)})
