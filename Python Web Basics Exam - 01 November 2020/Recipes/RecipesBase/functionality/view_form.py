from django.shortcuts import render, redirect

from RecipesBase.functionality.items import get_all_items
from RecipesBase.recipes_app.models import RecipeModel


def view_form(
        request='',
        base_form='',
        item_instance='',
        redirect_url='',
        base_url='',
        addition_data='',
        delete_form=False,
):
    if request.method == "GET":
        form = base_form(instance=item_instance if item_instance else None)

    else:
        form = base_form(request.POST, instance=item_instance if item_instance else None)
        if form.is_valid() or delete_form:
            form.save()
            return redirect(redirect_url)

    context = {
        "form": form,
        'recipes': get_all_items(RecipeModel)}

    if addition_data:
        context.update(addition_data)

    return render(request, base_url, context)
