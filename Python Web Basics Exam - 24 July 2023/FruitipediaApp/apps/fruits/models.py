from django.core import validators
from django.db import models
from apps.functionality.custom_validators import CustomValidators as cv


# Create your models here.


class FruitsModel(models.Model):

    name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        verbose_name="Fruit Name",
        validators=(validators.MinLengthValidator(2), cv.fruit_full_name_letters_only),
    )

    image_url = models.URLField(blank=False, null=False, verbose_name="Fruit Image URL")

    description = models.TextField(
        blank=False, null=False, verbose_name="Fruit Description"
    )

    nutrition = models.TextField(blank=True, null=True, verbose_name="Nutrition Info")

    def short_description(self):
        return (
            self.description
            if len(self.description) <= 50
            else f"{self.description[:51]}..."
        )
