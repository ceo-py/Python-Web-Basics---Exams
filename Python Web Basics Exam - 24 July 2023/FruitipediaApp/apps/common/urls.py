from django.urls import path

from apps.common.views import index, dashboard

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
]
