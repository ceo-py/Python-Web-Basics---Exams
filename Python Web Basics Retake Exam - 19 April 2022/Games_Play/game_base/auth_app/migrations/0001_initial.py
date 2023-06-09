# Generated by Django 4.0.3 on 2023-04-06 08:27

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
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(12)])),
                ('password', models.CharField(max_length=30)),
                ('first_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_Picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
