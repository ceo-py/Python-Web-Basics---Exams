from django.contrib import admin

from apps.fruits.models import FruitsModel
from apps.user_profile.models import ProfileModel

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(FruitsModel)