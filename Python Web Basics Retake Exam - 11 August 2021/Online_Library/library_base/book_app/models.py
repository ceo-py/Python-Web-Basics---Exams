from django.db import models


class BookModel(models.Model):

    title = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    description = models.TextField(
        blank=False,
        null=False,
        max_length=30,
    )

    image = models.URLField(
        blank=False,
        null=False,
    )

    type = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )