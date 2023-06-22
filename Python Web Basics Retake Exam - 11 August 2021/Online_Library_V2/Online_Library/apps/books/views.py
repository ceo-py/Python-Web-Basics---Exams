from django.shortcuts import redirect

from apps.books.forms import BookModelBaseForm
from apps.books.models import BookModel
from apps.functionality.get_profile import get_profile
from apps.functionality.items import find_item
from apps.functionality.view_form import view_form
from apps.user_profile.models import ProfileModel


# Create your views here.


def book_add(request):
    profile = get_profile(ProfileModel)

    return view_form(
        request=request,
        base_form=BookModelBaseForm,
        redirect_url='index',
        base_url='books/add-book.html',
        addition_data={
            'profile': profile
        }
    )


def book_edit(request, pk):
    profile = get_profile(ProfileModel)
    book = find_item(BookModel, pk)

    return view_form(
        request=request,
        base_form=BookModelBaseForm,
        item_instance=book,
        redirect_url='index',
        base_url='books/edit-book.html',
        addition_data={
            'profile': profile,
            'book': book
        }
    )


def book_details(request, pk):
    book = find_item(BookModel, pk)

    return view_form(
        request=request,
        base_form=BookModelBaseForm,
        item_instance=book,
        redirect_url='index',
        base_url='books/book-details.html',
        addition_data={
            'profile': get_profile(ProfileModel),
            'book': book
        }
    )


def book_delete(request, pk):
    find_item(BookModel, pk).delete()
    return redirect('index')
