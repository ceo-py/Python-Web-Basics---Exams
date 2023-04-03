from django.contrib import admin
from django.urls import include, path
from . import views

'''
http://localhost:8000/ - home page
http://localhost:8000/catalogue/ - catalogue
http://localhost:8000/create/ - plant create page
http://localhost:8000/details/<plant_id>/ - plant details page
http://localhost:8000/edit/<plant_id>/ - plant edit page
http://localhost:8000/delete/<plant_id>/ - plant delete page
http://localhost:8000/profile/create/ - profile create page
http://localhost:8000/profile/details/ - profile details page
http://localhost:8000/profile/edit/ - profile edit page
http://localhost:8000/profile/delete/ - profile delete page
'''

urlpatterns = [
    path('', views.home_page, name='index'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.plant_create, name='plant_create'),
    path('edit/<int:pk>/', views.plant_edit, name='plant_edit'),
    path('delete/<int:pk>/', views.plant_delete, name='plant_delete'),
    path('details/<int:pk>/', views.plant_details, name='plant_details'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile_create'),
        path('details/', views.profile_details, name='profile_details'),
        path('edit/', views.profile_edit, name='profile_edit'),
        path('delete/', views.profile_delete, name='profile_delete'),
    ])),
    path('admin/', admin.site.urls),
]
