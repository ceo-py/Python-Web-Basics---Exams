from django.urls import path

from apps.recipes.views import recipes_create, recipes_edit, recipes_delete, recipes_details

urlpatterns = [
    path("create/", recipes_create, name='recipes_create'),
    path("edit/<int:pk>/", recipes_edit, name='recipes_edit'),
    path("delete/<int:pk>/", recipes_delete, name='recipes_delete'),
    path("details/<int:pk>/", recipes_details, name='recipes_details'),
]
