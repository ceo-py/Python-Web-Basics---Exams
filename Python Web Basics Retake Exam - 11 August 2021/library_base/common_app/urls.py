
from django.urls import path

from library_base.common_app.views import index

urlpatterns = [
    path('', index, name='index')
]

