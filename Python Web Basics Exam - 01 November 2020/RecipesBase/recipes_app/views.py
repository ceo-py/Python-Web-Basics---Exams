from RecipesBase.functionality.items import get_all_items, find_item
from RecipesBase.functionality.view_form import view_form
from RecipesBase.recipes_app.forms import RecipeModelBaseForm, RecipeDeleteForm
from RecipesBase.recipes_app.models import RecipeModel


def recipe_create(request):

    return view_form(
        request=request,
        base_form=RecipeModelBaseForm,
        redirect_url='index',
        base_url='recipes_app/create.html',
    )


def recipe_edit(request, pk):
    recipe = find_item(RecipeModel, pk)

    return view_form(
        request=request,
        base_form=RecipeModelBaseForm,
        item_instance=recipe,
        redirect_url='index',
        base_url='recipes_app/edit.html',
        addition_data={'recipe': recipe}
    )


def recipe_delete(request, pk):
    recipe = find_item(RecipeModel, pk)

    return view_form(
        request=request,
        base_form=RecipeDeleteForm,
        item_instance=recipe,
        redirect_url='index',
        base_url='recipes_app/delete.html',
        addition_data={'recipe': recipe},
        delete_form=True,
    )


def recipe_details(request, pk):
    recipe = find_item(RecipeModel, pk)
    more_info = {
        'recipe': recipe,
        'ingredients': recipe.ingredients.split(', ')
    }
    return view_form(
        request=request,
        base_form=RecipeModelBaseForm,
        item_instance=recipe,
        redirect_url='index',
        base_url='recipes_app/details.html',
        addition_data=more_info
    )
