from django.core import validators
from django.db import models

from apps.functionality.capital_letter import validate_plant_name


# Create your models here.


class PlantsModel(models.Model):
    PLANT_CHOICES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants")
    )

    plant_type = models.CharField(
        max_length=14,
        verbose_name='Type',
        choices=PLANT_CHOICES
    )

    name = models.CharField(
        max_length=20,
        verbose_name='Name',
        validators=(
            validators.MinLengthValidator(2),
            validate_plant_name
        )
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField(
        verbose_name='Description'
    )

    price = models.FloatField(
        verbose_name='Price'
    )

    def catalogue_description(self):
        return self.description if len(self.description) <= 20 else f'{self.description[:21]}...'

    def price_format(self):
        return f'{self.price:.2f}'
