from django.contrib import admin

from My_Music_App.album.models import Album
from My_Music_App.user_profile.models import ProfileModel

# Register your models here.

admin.site.register(Album)
admin.site.register(ProfileModel)
