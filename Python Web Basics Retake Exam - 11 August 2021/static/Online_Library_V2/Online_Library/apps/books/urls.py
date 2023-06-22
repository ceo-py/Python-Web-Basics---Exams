from django.urls import path
from apps.books.views import book_add, book_edit, book_details, book_delete

urlpatterns = [
    path("add/", book_add, name='book_add'),
    path("edit/<int:pk>", book_edit, name='book_edit'),
    path("details/<int:pk>", book_details, name='book_details'),
    path("<int:pk>", book_delete, name='book_delete'),
]
