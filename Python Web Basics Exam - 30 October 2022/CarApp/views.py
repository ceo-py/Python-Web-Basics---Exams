from django.shortcuts import render, redirect

from CarApp.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from CarApp.models import ProfileModel, CarModel


def get_profile():
    try:
        return ProfileModel.objects.get()
    except ProfileModel.DoesNotExist as ex:
        return None


def get_cars():
    return CarModel.objects.all()


def create_context(profile):
    return {
        'profile': profile
    }


def delete_all_cars(cars, request):
    for car in cars:
        form = CarDeleteForm(request.POST, instance=car)
        form.save()


def index(request):
    context = create_context(get_profile())

    return render(request, 'CarrApp/index.html', context)


def catalogue(request):
    context = create_context(get_profile())
    context['cars'] = sorted(get_cars(), key=lambda x: x.pk)
    context['cars_counter'] = len(context['cars'])

    return render(request, 'CarrApp/catalogue.html', context)


def profile_create(request):
    context = create_context(get_profile())

    if context['profile'] is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()

    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context['form'] = form
    return render(request, 'CarrApp/profile/profile-create.html', context)


def profile_details(request):
    context = create_context(get_profile())
    context['cars_total_price'] = sum(car.price for car in get_cars())
    context['name'] = (' ').join\
        ([name for name in [context['profile'].first_Name, context['profile'].last_Name] if
          name is not None])

    return render(request, 'CarrApp/profile/profile-details.html', context)


def profile_edit(request):
    context = create_context(get_profile())

    if request.method == 'GET':
        form = ProfileEditForm(instance=context['profile'])

    else:
        form = ProfileEditForm(request.POST, instance=context['profile'])
        if form.is_valid():
            form.save()
            return redirect('profile_details')

    context['form'] = form
    return render(request, 'CarrApp/profile/profile-edit.html', context)


def profile_delete(request):
    context = create_context(get_profile())

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=context['profile'])
        form.save()
        delete_all_cars(get_cars(), request)

        return redirect('index')

    return render(request, 'CarrApp/profile/profile-delete.html', context)


def car_create(request):
    context = create_context(get_profile())

    if request.method == 'GET':
        form = CarCreateForm()

    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context['form'] = form

    return render(request, 'CarrApp/car/car-create.html', context)


def car_details(request, pk):
    context = create_context(get_profile())
    context['car'] = CarModel.objects.filter(pk=pk).get()

    return render(request, 'CarrApp/car/car-details.html', context)


def car_edit(request, pk):
    context = create_context(get_profile())
    context['car'] = CarModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarEditForm(instance=context['car'])

    else:
        form = CarEditForm(request.POST, instance=context['car'])
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context['form'] = form

    return render(request, 'CarrApp/car/car-edit.html', context)


def car_delete(request, pk):
    context = create_context(get_profile())
    context['car'] = CarModel.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=context['car'])

    else:
        form = CarDeleteForm(request.POST, instance=context['car'])
        form.save()
        return redirect('catalogue')

    context['form'] = form

    return render(request, 'CarrApp/car/car-delete.html', context)

