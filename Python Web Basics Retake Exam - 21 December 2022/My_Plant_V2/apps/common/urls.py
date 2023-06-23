from django.urls import path
from apps.common.views import index, catalogue

urlpatterns = [
    path("", index, name='index'),
    path("catalogue/", catalogue, name='catalogue'),
]
