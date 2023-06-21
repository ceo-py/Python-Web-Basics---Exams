from django.db import models
from django.core import validators
import My_Music_App.functionality.custom_validations as cv


# Create your models here.


class ProfileModel(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            cv.validate_username,
        ),
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=True, null=True, validators=(validators.MinValueValidator(0),)
    )
