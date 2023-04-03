from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_username_min_chars(value):
    if len(value) <= 1:
        raise ValidationError('The username must be a minimum of 2 chars')


def validate_correct_car_year(value):
    if not 1980 <= int(value) <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')


class ProfileModel(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    AGE_MIN_VALUE = 18
    PASSWORD_MAX_LEN = 30
    NAME_MAX_LEN = 30

    username = models.CharField(
        blank=False,
        null=False,
        max_length=USERNAME_MAX_LEN,
        validators=(
            validate_username_min_chars,
        ),
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(validators.MinValueValidator(AGE_MIN_VALUE),),
    )

    password = models.CharField(
        blank=False,
        null=False,
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=NAME_MAX_LEN,
        verbose_name='First Name',

    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=NAME_MAX_LEN,
        verbose_name='Last Name',
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name='Profile Picture',
    )


class CarModel(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2

    SPORT_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CARS = (
        (SPORT_CAR, SPORT_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        blank=False,
        null=False,
        max_length=TYPE_MAX_LEN,
        choices=CARS,
    )

    model = models.CharField(
        blank=False,
        null=False,
        max_length=MODEL_MAX_LEN,
        validators=(validators.MinLengthValidator(MODEL_MIN_LEN),),
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validate_correct_car_year,),
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(validators.MinValueValidator(1),),
    )
