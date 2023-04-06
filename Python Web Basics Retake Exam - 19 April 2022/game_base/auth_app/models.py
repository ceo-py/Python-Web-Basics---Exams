from django.core import validators
from django.db import models


class ProfileModel(models.Model):

    email = models.EmailField(
        null=False,
        blank=False,

    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(12),
        ),
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    first_Name = models.CharField(
        null=True,
        blank=True,
        max_length=30,

    )

    last_Name = models.CharField(
        null=True,
        blank=True,
        max_length=30,

    )

    profile_Picture = models.URLField(
        null=True,
        blank=True,
    )