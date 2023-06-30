
from django.contrib import admin
from django.urls import path, include

from apps.books.views import *

urlpatterns = [
    path('add/', book_add, name='book_add'),
    path('edit/<int:pk>/', book_edit, name='book_edit'),
    path('details/<int:pk>/', book_details, name='book_details'),
    path('delete/<int:pk>/', book_delete, name='book_delete'),
]
