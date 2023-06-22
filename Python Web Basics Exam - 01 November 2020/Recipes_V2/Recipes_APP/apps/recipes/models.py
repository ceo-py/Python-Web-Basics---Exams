from django.db import models


# Create your models here.


class RecipesModel(models.Model):

    title = models.CharField(
        max_length=30,
        verbose_name='Title'
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField(
        verbose_name='Description'
    )

    ingredients = models.CharField(
        max_length=250,
        verbose_name='Ingredients'
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)'
    )
