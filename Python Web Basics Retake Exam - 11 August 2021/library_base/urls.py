"""
URL configuration for library_base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from library_base.book_app.views import book_add, book_edit, book_details, book_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('library_base.common_app.urls')),
    path("profile/", include('library_base.auth_app.urls')),
    path("add/", book_add, name='book_add'),
    path("edit<int:pk>/", book_edit, name='book_edit'),
    path("details<int:pk>/", book_details, name='book_details'),
    path('<int:pk>/', book_delete, name='book_delete'),
]
