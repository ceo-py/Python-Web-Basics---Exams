from django.core import validators
from django.db import models

from apps.functionality.capital_letter import validate_user_name


# Create your models here.


class ProfileModel(models.Model):

    username = models.CharField(
        max_length=20,
        verbose_name='Username',
        validators=(
            validators.MinLengthValidator(2),
        )
    )

    first_name = models.CharField(
        max_length=20,
        verbose_name='First Name',
        validators=(
            validate_user_name,
        )
    )

    last_name = models.CharField(
        max_length=20,
        verbose_name='Last Name',
        validators=(
            validate_user_name,
        )
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture'
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
