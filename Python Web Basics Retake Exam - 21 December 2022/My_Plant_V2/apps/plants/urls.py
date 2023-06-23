from django.urls import path

from apps.plants.views import plant_create, plant_details, plant_edit, plant_delete

urlpatterns = [
    path("create/", plant_create, name='plant_create'),
    path("details/<int:pk>/", plant_details, name='plant_details'),
    path("edit/<int:pk>/", plant_edit, name='plant_edit'),
    path("delete/<int:pk>/", plant_delete, name='plant_delete'),
]
