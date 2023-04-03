from django.contrib import admin

from myPlantApp.models import ProfileModel, PlantModel


@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(PlantModel)
class PlantAdmin(admin.ModelAdmin):
    pass