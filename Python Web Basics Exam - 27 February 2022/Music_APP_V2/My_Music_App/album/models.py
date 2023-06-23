from django.db import models
from django.core import validators


# Create your models here.


class Album(models.Model):
    GENRE_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]

    album_name = models.CharField(
        max_length=30,
        verbose_name='Album Name',
        unique=True,
    )

    artist = models.CharField(
        blank=False,
        null=False,
        verbose_name='Artist',
        max_length=30,
    )

    genre = models.CharField(
        blank=False,
        null=False,
        verbose_name='Genre',
        max_length=30,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        verbose_name='Description',
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=(
            validators.MinValueValidator(0.0),
        )

    )

