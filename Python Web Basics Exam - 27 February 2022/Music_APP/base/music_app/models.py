from django.core import validators
from django.db import models


class AlbumModel(models.Model):

    album_Name = models.CharField(
        blank=False,
        null=False,
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        choices=(
            ("Pop Music", "Pop Music"),
            ("Jazz Music", "Jazz Music"),
            ("R&B Music", "R&B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music", "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip Hop Music", "Hip Hop Music"),
            ("Other", "Other"),
        ),
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_URL = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(validators.MinValueValidator(0.0),),
    )
