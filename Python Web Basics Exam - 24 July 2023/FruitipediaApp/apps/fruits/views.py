from django.shortcuts import render

from apps.fruits.forms import (
    FruitsCreateForm,
    FruitsModelBaseForm,
    FruitsEditForm,
    FruitsDeleteForm,
)
from apps.fruits.models import FruitsModel
from apps.functionality.items import find_item
from apps.functionality.profile_exist import check_profile_exists
from apps.functionality.view_form import view_form


# Create your views here.
@check_profile_exists
def fruit_create(request):
    return view_form(
        request=request,
        base_form=FruitsCreateForm,
        redirect_url="dashboard",
        base_url="fruits/create-fruit.html",
    )


@check_profile_exists
def fruit_details(request, pk):
    return render(
        request, "fruits/details-fruit.html", {"fruit": find_item(FruitsModel, pk)}
    )


@check_profile_exists
def fruit_edit(request, pk):
    fruit = find_item(FruitsModel, pk)
    return view_form(
        request=request,
        item_instance=fruit,
        base_form=FruitsEditForm,
        redirect_url="dashboard",
        base_url="fruits/edit-fruit.html",
        addition_data={"fruit": fruit},
    )


@check_profile_exists
def fruit_delete(request, pk):
    fruit = find_item(FruitsModel, pk)
    return view_form(
        request=request,
        item_instance=fruit,
        base_form=FruitsDeleteForm,
        redirect_url="dashboard",
        base_url="fruits/delete-fruit.html",
        delete_form=True,
        addition_data={"fruit": fruit},
    )
