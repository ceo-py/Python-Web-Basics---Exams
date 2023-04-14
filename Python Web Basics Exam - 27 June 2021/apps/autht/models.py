from django.db import models


class ProfileModel(models.Model):

    first_name = models.CharField(
        max_length=20,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=20,
        verbose_name='Last Name'
    )

    age = models.IntegerField()

    image_url = models.URLField(
        verbose_name='Link to Profile Image',
    )

