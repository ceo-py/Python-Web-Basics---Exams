from django.shortcuts import render, redirect

from library_base.auth_app.models import ProfileModel
from library_base.book_app.forms import BookModelBaseForm
from library_base.book_app.models import BookModel
from library_base.functionality.items import find_item
from library_base.functionality.profile import get_profile
from library_base.functionality.view_form import view_form


def book_add(request):
    return view_form(
        request=request,
        base_form=BookModelBaseForm,
        redirect_url='index',
        base_url='book_app/add-book.html',
        addition_data={'profile': get_profile(ProfileModel)},
    )


def book_edit(request, pk):
    book = find_item(BookModel, pk)
    return view_form(
        request=request,
        base_form=BookModelBaseForm,
        item_instance=book,
        redirect_url='index',
        base_url='book_app/edit-book.html',
        addition_data={
            'profile': get_profile(ProfileModel),
        'book': book},
    )


def book_details(request, pk):

    context = {
        'book': find_item(BookModel, pk),
        'profile': get_profile(ProfileModel)
    }

    return render(request, 'book_app/book-details.html', context)


def book_delete(request, pk):
    book = find_item(BookModel, pk)
    book.delete()
    return redirect('index')