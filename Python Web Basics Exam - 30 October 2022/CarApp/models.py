from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_min_characters_in_string(value):
    if not len(value) >= 2:
        raise ValidationError("The username must be a minimum of 2 chars")


def validate_year_between_1980_2049(value):
    if not 1980 <= int(value) <= 2049:
        raise ValidationError("Year must be between 1980 and 2049")


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
        validators=(validate_min_characters_in_string,),
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

    first_Name = models.CharField(
        blank=True,
        null=True,
        max_length=NAME_MAX_LEN,
    )

    last_Name = models.CharField(
        blank=True,
        null=True,
        max_length=NAME_MAX_LEN,
    )

    profile_Picture = models.URLField(
        blank=True,
        null=True,
    )


class CarModel(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2
    PRICE_MIN_VALUE = 1

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
        validators=(validators.MinLengthValidator(MODEL_MIN_LEN),)

    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(validate_year_between_1980_2049,),
    )

    image_URL = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(validators.MinValueValidator(PRICE_MIN_VALUE),),
    )
