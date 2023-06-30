from django.shortcuts import render, redirect

from apps.books.forms import BooksCreateForm, BooksModelBaseForm
from apps.books.models import BooksModel
from apps.functionality.deco_profile import check_profile_exists
from apps.functionality.get_profile import get_profile
from apps.functionality.items import find_item
from apps.functionality.view_form import view_form
from apps.user_profile.models import ProfileModel


# Create your views here.
@check_profile_exists
def book_add(request):
    profile = get_profile(ProfileModel)

    return view_form(
        request=request,
        base_form=BooksCreateForm,
        redirect_url='index',
        base_url='books/add-book.html',
        addition_data={
            'profile': profile
        }
    )

@check_profile_exists
def book_edit(request, pk):
    profile = get_profile(ProfileModel)
    book = find_item(BooksModel, pk)

    return view_form(
        request=request,
        base_form=BooksModelBaseForm,
        item_instance=book,
        redirect_url='index',
        base_url='books/edit-book.html',
        addition_data={
            'profile': profile,
            'book': book,
        }
    )

@check_profile_exists
def book_details(request, pk):
    book = find_item(BooksModel, pk)
    profile = get_profile(ProfileModel)

    return render(request, 'books/book-details.html', context={
        'book': book,
        'profile': profile
    })

@check_profile_exists
def book_delete(request, pk):
    find_item(BooksModel, pk).delete()
    return redirect('index')

