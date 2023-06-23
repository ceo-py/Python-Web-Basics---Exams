from django.contrib import admin

from apps.plants.models import PlantsModel
from apps.user_profile.models import ProfileModel

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(PlantsModel)