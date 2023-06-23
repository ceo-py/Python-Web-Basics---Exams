from django.db import models


class ProfileModel(models.Model):
    first_Name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    last_Name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )

    image_URL = models.URLField(
        null=False,
        blank=False,
    )
