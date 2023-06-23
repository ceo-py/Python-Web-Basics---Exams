"""
URL configuration for game_base project.

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
from game_base.game_app.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('game_base.common_app.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include('game_base.auth_app.urls')),
    path('game/', include('game_base.game_app.urls')),
]
