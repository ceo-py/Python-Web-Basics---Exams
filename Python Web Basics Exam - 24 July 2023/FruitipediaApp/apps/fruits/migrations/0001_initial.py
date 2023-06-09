# Generated by Django 4.2 on 2023-06-24 06:28

import apps.functionality.custom_validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FruitsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            apps.functionality.custom_validators.CustomValidators.fruit_full_name_letters_only,
                        ],
                        verbose_name="Fruit Name",
                    ),
                ),
                ("image_url", models.URLField(verbose_name="Fruit Image URL")),
                ("description", models.TextField(verbose_name="Fruit Description")),
                (
                    "nutrition",
                    models.TextField(
                        blank=True, null=True, verbose_name="Nutrition Info"
                    ),
                ),
            ],
        ),
    ]
