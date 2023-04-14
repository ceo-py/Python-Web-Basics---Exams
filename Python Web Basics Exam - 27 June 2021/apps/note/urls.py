"""
URL configuration for note_base project.

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

from django.urls import path
from apps.note.views import note_create, note_edit, note_delete, note_details

urlpatterns = [
    path("add/", note_create, name='note_create'),
    path("edit/<int:pk>/", note_edit, name='note_edit'),
    path("delete/<int:pk>/", note_delete, name='note_delete'),
    path("details/<int:pk>/", note_details, name='note_details'),
]
