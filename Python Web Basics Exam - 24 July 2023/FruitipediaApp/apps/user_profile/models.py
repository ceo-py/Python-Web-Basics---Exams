from django.core import validators
from django.db import models

from apps.functionality.custom_validators import CustomValidators as cv


# Create your models here.


class ProfileModel(models.Model):
    first_name = models.CharField(
        max_length=25,
        verbose_name="First Name",
        blank=False,
        null=False,
        validators=(validators.MinLengthValidator(2), cv.letter_start),
    )

    last_name = models.CharField(
        max_length=35,
        verbose_name="Last Name",
        blank=False,
        null=False,
        validators=(validators.MinLengthValidator(1), cv.letter_start),
    )

    email = models.EmailField(
        max_length=40,
        verbose_name="Email",
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=20,
        verbose_name="Password",
        blank=False,
        null=False,
        validators=(validators.MinLengthValidator(8),),
    )

    image_url = models.URLField(blank=True, null=True, verbose_name="Image URL")

    age = models.IntegerField(blank=True, null=True, verbose_name="Age", default=18)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
