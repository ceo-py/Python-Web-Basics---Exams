from django.db import models


# Create your models here.


class BookModel(models.Model):

    title = models.CharField(
        max_length=30,
        verbose_name='Title'
    )

    description = models.TextField(
        verbose_name='Description'
    )

    image = models.URLField(
        verbose_name='Image'
    )

    type = models.CharField(
        max_length=30,
        verbose_name='Type'
    )
