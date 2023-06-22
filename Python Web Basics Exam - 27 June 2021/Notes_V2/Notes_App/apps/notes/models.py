from django.db import models


# Create your models here.


class NotesModel(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='Title'
    )

    image_url = models.URLField(
        verbose_name='Link to Image'
    )

    content = models.TextField(
        verbose_name='Content'
    )
