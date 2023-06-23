from django.contrib import admin

from apps.game.models import GameModel
from apps.user_profile.models import ProfileModel

# Register your models here.

admin.site.register(ProfileModel)
admin.site.register(GameModel)