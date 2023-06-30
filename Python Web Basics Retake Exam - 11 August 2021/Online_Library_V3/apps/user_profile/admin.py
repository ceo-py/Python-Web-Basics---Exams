from django.contrib import admin

from apps.books.models import BooksModel
from apps.user_profile.models import ProfileModel

# Register your models here.

admin.site.register((
    BooksModel, ProfileModel
))
