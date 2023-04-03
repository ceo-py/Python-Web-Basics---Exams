"""CarApp URL Configuration

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
from CarApp import views
from base.urls import include

'''
http://localhost:8000/car/create/ - car create page
http://localhost:8000/car/<car-id>/details/ - car details page
http://localhost:8000/car/<car-id>/edit/ - car edit page
http://localhost:8000/car/<car-id>/delete/ - car delete page
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile_create'),
        path('details/', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ])),
    path('car/', include([
        path('/create/', views.car_create, name='car_create'),
        path('<int:pk>details/', views.car_details, name='car_details'),
        path('<int:pk>edit/', views.car_edit, name='car_edit'),
        path('<int:pk>delete/', views.car_delete, name='car_delete'),
    ]))
]
