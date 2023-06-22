from apps.functionality.items import find_item
from apps.functionality.view_forms import view_form
from apps.recipes.forms import RecipesModelBaseForm, RecipesDeleteForm
from apps.recipes.models import RecipesModel


# Create your views here.

def recipes_create(request):

    return view_form(
        request=request,
        base_form=RecipesModelBaseForm,
        redirect_url='index',
        base_url='recipes/create.html',
    )


def recipes_edit(request, pk):
    recipe = find_item(RecipesModel, pk)
    return view_form(
        request=request,
        item_instance=recipe,
        base_form=RecipesModelBaseForm,
        redirect_url='index',
        base_url='recipes/edit.html',
        addition_data={
            'recipe': recipe
        }
    )


def recipes_delete(request, pk):
    recipe = find_item(RecipesModel, pk)

    return view_form(
        request=request,
        item_instance=recipe,
        base_form=RecipesDeleteForm,
        redirect_url='index',
        base_url='recipes/delete.html',
        delete_form=True,
        addition_data={
            'recipe': recipe
        }
    )


def recipes_details(request, pk):
    recipe = find_item(RecipesModel, pk)
    return view_form(
        request=request,
        item_instance=recipe,
        base_form=RecipesModelBaseForm,
        redirect_url='index',
        base_url='recipes/details.html',
        addition_data={
            'recipe': recipe,
            'ingredients': recipe.ingredients.split(', ')
        }
    )
