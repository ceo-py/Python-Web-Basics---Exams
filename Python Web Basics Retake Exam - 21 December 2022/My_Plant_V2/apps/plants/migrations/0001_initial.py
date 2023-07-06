# Generated by Django 4.2 on 2023-06-22 13:20

import apps.functionality.capital_letter
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlantsModel",
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
                    "plant_type",
                    models.CharField(
                        choices=[
                            ("Outdoor Plants", "Outdoor Plants"),
                            ("Indoor Plants", "Indoor Plants"),
                        ],
                        max_length=14,
                        verbose_name="Type",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.MinValueValidator(2),
                            apps.functionality.capital_letter.validate_plant_name,
                        ],
                        verbose_name="Name",
                    ),
                ),
                ("image_url", models.URLField(verbose_name="Image URL")),
                ("description", models.TextField(verbose_name="Description")),
                ("price", models.FloatField(verbose_name="Price")),
            ],
        ),
    ]