"""game_app URL Configuration

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

from base.game_app import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.game_create, name='game_create'),
    path('details/<int:pk>', views.game_details, name='game_details'),
    path('edit/<int:pk>', views.game_edit, name='game_edit'),
    path('delete/<int:pk>', views.game_delete, name='game_delete'),
]
