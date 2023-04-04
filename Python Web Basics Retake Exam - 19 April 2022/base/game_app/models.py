from django.core import validators
from django.db import models


class GameModel(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        unique=True,
    )

    category = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        choices=(
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", "Board/Card Game"),
            ("Other", "Other"),
        )
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5.0)
        ),
    )

    max_Level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            validators.MinValueValidator(1),
        ),
    )

    image_URL = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )