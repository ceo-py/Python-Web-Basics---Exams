from django.db import models


class RecipeModel(models.Model):

    title = models.CharField(
        max_length=30,
    )

    image_url = models.URLField(
        verbose_name='Image URL',
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=250,
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)',
    )
