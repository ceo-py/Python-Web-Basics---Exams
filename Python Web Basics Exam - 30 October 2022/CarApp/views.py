from django.shortcuts import render, redirect

from CarApp.forms import ProfileCreateModel, ProfileEditModel, ProfileDeleteModel, CarCreateModel, CarEditModel, \
    CarDeleteModel
from CarApp.models import ProfileModel, CarModel


def get_profile() -> ProfileModel:
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def get_cars() -> CarModel:
    return CarModel.objects.all()


def generate_profile_context(profile: ProfileModel) -> dict:
    return {
        'profile': profile
    }


def delete_all_cars(cars, request):
    for car in cars:
        plant_form = ProfileDeleteModel(request.POST, instance=car)
        plant_form.save()


def index(request):
    context = generate_profile_context(get_profile())

    return render(request, 'CarApp/index.html', context)


def catalogue(request):
    context = generate_profile_context(get_profile())
    context['cars'] = get_cars()
    context['car_count'] = len(context['cars'])

    return render(request, 'CarApp/catalogue.html', context)


def profile_create(request):
    context = generate_profile_context(get_profile())

    if context['profile'] is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateModel()

    else:
        form = ProfileCreateModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context['form'] = form
    return render(request, 'CarApp/profile/profile-create.html', context)


def profile_details(request):
    context = generate_profile_context(get_profile())
    context['cars_total_price'] = sum(car.price for car in get_cars())
    context['name'] = (' ').join(
        [name for name in [context['profile'].first_name, context['profile'].last_name] if name is not None])
    return render(request, 'CarApp/profile/profile-details.html', context)


def profile_edit(request):
    context = generate_profile_context(get_profile())

    if request.method == 'GET':
        form = ProfileEditModel(instance=context['profile'])

    else:
        form = ProfileEditModel(request.POST, instance=context['profile'])
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context['form'] = form

    return render(request, 'CarApp/profile/profile-edit.html', context)


def profile_delete(request):
    context = generate_profile_context(get_profile())

    if request.method == 'POST':
        form = ProfileDeleteModel(request.POST, instance=context['profile'])
        form.save()
        delete_all_cars(get_cars(), request)

        return redirect('index')



    return render(request, 'CarApp/profile/profile-delete.html', context)


def car_create(request):
    context = generate_profile_context(get_profile())

    if request.method == 'GET':
        form = CarCreateModel()

    else:
        form = CarCreateModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context['form'] = form

    return render(request, 'CarApp/car/car-create.html', context)


def car_details(request, pk):
    context = generate_profile_context(get_profile())
    context['car'] = CarModel.objects.filter(pk=pk).get()

    return render(request, 'CarApp/car/car-details.html', context)


def car_edit(request, pk):
    context = generate_profile_context(get_profile())
    context['car'] = CarModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarEditModel(instance=context['car'])

    else:
        form = CarEditModel(request.POST, instance=context['car'])
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context['form'] = form

    return render(request, 'CarApp/car/car-edit.html', context)


def car_delete(request, pk):
    context = generate_profile_context(get_profile())
    context['car'] = CarModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDeleteModel(instance=context['car'])

    else:
        form = CarDeleteModel(request.POST, instance=context['car'])
        form.save()
        return redirect('catalogue')

    context['form'] = form

    return render(request, 'CarApp/car/car-delete.html', context)
