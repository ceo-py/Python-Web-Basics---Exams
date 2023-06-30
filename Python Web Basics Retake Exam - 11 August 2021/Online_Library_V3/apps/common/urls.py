from django.urls import path, include

from apps.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
