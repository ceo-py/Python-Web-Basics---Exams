
from django.contrib import admin
from django.urls import path, include

from RecipesBase.recipes_app.views import recipe_create, recipe_edit, recipe_delete, recipe_details

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("RecipesBase.common_app.urls")),
    path("create/", recipe_create, name='recipe_create'),
    path("edit/<int:pk>", recipe_edit, name='recipe_edit'),
    path("delete/<int:pk>", recipe_delete, name='recipe_delete'),
    path("details/<int:pk>", recipe_details, name='recipe_details'),
]
