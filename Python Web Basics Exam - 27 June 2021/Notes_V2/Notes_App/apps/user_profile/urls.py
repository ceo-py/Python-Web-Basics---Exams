from django.urls import path
from apps.user_profile.views import profile_details, profile_delete

urlpatterns = [
    path("profile", profile_details, name='profile_details'),
    path("", profile_delete, name='profile_delete'),
]
