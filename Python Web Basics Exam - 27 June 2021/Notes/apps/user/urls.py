from django.urls import path

from apps.user.views import user_profile, user_profile_delete

urlpatterns = [
    path('profile/', user_profile, name='user_profile'),
    path('profile/delete', user_profile_delete, name='user_profile_delete'),
]
