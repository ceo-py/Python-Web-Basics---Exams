# Generated by Django 4.0.3 on 2023-04-03 18:54

import CarApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[CarApp.models.validate_username_min_chars])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]
