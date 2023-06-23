# Generated by Django 4.2 on 2023-06-22 13:20

import apps.functionality.capital_letter
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProfileModel",
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
                    "username",
                    models.CharField(
                        max_length=20,
                        validators=[django.core.validators.MinLengthValidator(2)],
                        verbose_name="Username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=20,
                        validators=[
                            apps.functionality.capital_letter.validate_user_name
                        ],
                        verbose_name="First Name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=20,
                        validators=[
                            apps.functionality.capital_letter.validate_user_name
                        ],
                        verbose_name="Last Name",
                    ),
                ),
                (
                    "profile_picture",
                    models.URLField(
                        blank=True, null=True, verbose_name="Profile Picture"
                    ),
                ),
            ],
        ),
    ]
