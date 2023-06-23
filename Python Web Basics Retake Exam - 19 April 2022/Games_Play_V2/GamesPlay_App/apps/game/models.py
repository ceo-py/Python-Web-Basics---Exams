from django.core import validators
from django.db import models


# Create your models here.
class GameModel(models.Model):
    GAME_OPTIONS = [
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other")
    ]

    title = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Title'
    )

    category = models.CharField(
        choices=GAME_OPTIONS,
        verbose_name='Category'
    )

    rating = models.FloatField(
        verbose_name='Rating',
        validators=(
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5.0),
        )
    )

    max_level = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Max Level',
        validators=(
            validators.MinValueValidator(1),
        )
    )

    image_url = models.URLField(
        verbose_name='Image Url'
    )

    summary = models.TextField(
        blank=True,
        null=True,
        verbose_name='Summary'
    )
