from django.urls import path, include

from apps.notes.views import note_add, note_edit, note_delete, note_details

urlpatterns = [
    path('add/', note_add, name='note_add'),
    path('edit/<int:pk>/', note_edit, name='note_edit'),
    path('delete/<int:pk>/', note_delete, name='note_delete'),
    path('details/<int:pk>/', note_details, name='note_details'),
]
