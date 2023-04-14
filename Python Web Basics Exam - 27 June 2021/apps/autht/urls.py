from django.urls import path

from apps.autht.views import profile, delete_profile

urlpatterns = [
    path("delete/", delete_profile, name='delete_profile'),
    path("", profile, name='profile'),
]
