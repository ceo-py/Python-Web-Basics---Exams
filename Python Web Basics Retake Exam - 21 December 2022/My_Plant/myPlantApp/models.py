from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

def validate_start_capital_letter(value):  # add code good practice
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def validate_only_alphanumeric(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


class ProfileModel(models.Model):
    USERNAME_NAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    username = models.CharField(
        max_length=USERNAME_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(USERNAME_MIN_LEN),
        ),
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validate_start_capital_letter,
        ),
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=(
            validate_start_capital_letter,
        ),
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )


class PlantModel(models.Model):
    PLANT_MAX_LEN = 14
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 2

    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'

    PLANTS = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=PLANT_MAX_LEN,
        choices=PLANTS,
        verbose_name='Type',
    )

    name = models.CharField(
        null=False,
        blank=False,
        max_length=NAME_MAX_LEN,
        validators=(validators.MinLengthValidator(NAME_MIN_LEN), validate_only_alphanumeric,),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )