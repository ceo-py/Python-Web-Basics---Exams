from django.shortcuts import render

from apps.functionality.items import find_item
from apps.functionality.profile_exist import check_profile_exists
from apps.functionality.view_form import view_form
from apps.plants.forms import PlantsModelBaseForm, PlantsDeleteForm
from apps.plants.models import PlantsModel


# Create your views here.
@check_profile_exists
def plant_create(request):
    return view_form(
        request=request,
        base_form=PlantsModelBaseForm,
        redirect_url='catalogue',
        base_url='plants/create-plant.html',
    )


@check_profile_exists
def plant_details(request, pk):
    return render(request, 'plants/plant-details.html', {'plant': find_item(PlantsModel, pk)})


@check_profile_exists
def plant_edit(request, pk):
    plant = find_item(PlantsModel, pk)
    return view_form(
        request=request,
        item_instance=plant,
        base_form=PlantsModelBaseForm,
        redirect_url='catalogue',
        base_url='plants/edit-plant.html',
        addition_data={
            'plant': plant
        }
    )


@check_profile_exists
def plant_delete(request, pk):
    plant = find_item(PlantsModel, pk)
    return view_form(
        request=request,
        item_instance=plant,
        base_form=PlantsDeleteForm,
        redirect_url='catalogue',
        base_url='plants/delete-plant.html',
        delete_form=True,
        addition_data={
            'plant': plant
        }
    )
