"""auth_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from game_base.auth_app.views import create_profile, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('create/', create_profile, name='profile_create'),
    path('details/', profile_details, name='profile_details'),
    path('edit/', profile_edit, name='profile_edit'),
    path('delete/', profile_delete, name='profile_delete'),
]
