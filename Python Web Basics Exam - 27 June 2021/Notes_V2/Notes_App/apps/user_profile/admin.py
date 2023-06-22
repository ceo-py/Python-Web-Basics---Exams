from django.contrib import admin

from apps.notes.models import NotesModel
from apps.user_profile.models import ProfileModel

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(NotesModel)
