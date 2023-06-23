
from django.contrib import admin
from django.urls import path
from apps.common.views import index

urlpatterns = [
    path("", index, name='index'),
]
