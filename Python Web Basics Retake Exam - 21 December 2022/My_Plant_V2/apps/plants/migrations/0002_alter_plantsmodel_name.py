# Generated by Django 4.2 on 2023-06-23 12:04

import apps.functionality.capital_letter
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plants", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plantsmodel",
            name="name",
            field=models.CharField(
                max_length=20,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    apps.functionality.capital_letter.validate_plant_name,
                ],
                verbose_name="Name",
            ),
        ),
    ]