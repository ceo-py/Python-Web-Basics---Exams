from django.shortcuts import render, redirect

from myPlantApp.forms import ProfileModelCreateForm, PlantModelCreateForm, PlantModelEditForm, PlantModelDeleteForm, \
    ProfileModelEditForm, ProfileModelDeleteForm
from myPlantApp.models import ProfileModel, PlantModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def get_plants():
    return PlantModel.objects.all().order_by('pk')


def delete_all_plants(plants, request):
    plants = get_plants()
    for plant in plants:
        plant_form = PlantModelDeleteForm(request.POST, instance=plant)
        plant_form.save()


def home_page(request):
    user = get_profile()
    context = {
        'user': user
    }

    return render(request, 'myPlantApp/home-page.html', context)


def catalogue(request):
    plants = sorted(get_plants(), key=lambda x: x.pk)

    context = {
        'plants': plants,
        'plants_available': len(plants),
    }
    return render(request, 'myPlantApp/catalogue.html', context)


def plant_create(request):
    if request.method == 'GET':
        form = PlantModelCreateForm()

    else:
        form = PlantModelCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form
    }
    return render(request, 'myPlantApp/plant/create-plant.html', context)


def plant_details(request, pk):
    plant = PlantModel.objects.filter(pk=pk).get()
    contex = {
        'plant': plant
    }

    return render(request, 'myPlantApp/plant/plant-details.html', contex)


def plant_edit(request, pk):
    plant = PlantModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PlantModelEditForm(instance=plant)
    else:
        form = PlantModelEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    contex = {
        'form': form,
        'plant': plant
    }
    return render(request, 'myPlantApp/plant/edit-plant.html', contex)


def plant_delete(request, pk):
    plant = PlantModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = PlantModelDeleteForm(instance=plant)
    else:
        form = PlantModelDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    contex = {
        'form': form,
        'plant': plant
    }
    return render(request, 'myPlantApp/plant/delete-plant.html', contex)


def profile_create(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileModelCreateForm()

    else:
        form = ProfileModelCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'myPlantApp/profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    plants = get_plants()

    contex = {
        'profile': profile,
        'plants': len(plants)
    }

    return render(request, 'myPlantApp/profile/profile-details.html', contex)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileModelEditForm(instance=profile)
    else:
        form = ProfileModelEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    contex = {
        'form': form,
    }

    return render(request, 'myPlantApp/profile/edit-profile.html', contex)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'POST':

        form = ProfileModelDeleteForm(request.POST, instance=profile)
        form.save()
        delete_all_plants(get_plants(), request)

        return redirect('index')

    return render(request, 'myPlantApp/profile/delete-profile.html')
