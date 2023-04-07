
from django.contrib import admin
from django.urls import path

from RecipesBase.common_app.views import index

urlpatterns = [
    path('', index, name="index"),
]
