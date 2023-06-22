from django.urls import path
from apps.notes.views import notes_add, notes_edit, notes_delete, notes_details

urlpatterns = [
    path("add/", notes_add, name='notes_add'),
    path("edit/<int:pk>", notes_edit, name='notes_edit'),
    path("delete/<int:pk>", notes_delete, name='notes_delete'),
    path("details/<int:pk>", notes_details, name='notes_details'),
]
