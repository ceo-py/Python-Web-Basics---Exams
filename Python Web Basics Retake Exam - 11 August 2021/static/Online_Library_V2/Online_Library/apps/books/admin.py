from django.contrib import admin

from apps.books.models import BookModel
from apps.user_profile.models import ProfileModel

# Register your models here.

admin.site.register(ProfileModel)
admin.site.register(BookModel)