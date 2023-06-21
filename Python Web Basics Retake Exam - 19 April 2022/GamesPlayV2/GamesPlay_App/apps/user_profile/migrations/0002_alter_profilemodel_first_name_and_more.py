# Generated by Django 4.2 on 2023-06-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilemodel",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="First Name"
            ),
        ),
        migrations.AlterField(
            model_name="profilemodel",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Last Name"
            ),
        ),
        migrations.AlterField(
            model_name="profilemodel",
            name="profile_picture",
            field=models.URLField(
                blank=True, null=True, verbose_name="Profile Picture"
            ),
        ),
    ]
