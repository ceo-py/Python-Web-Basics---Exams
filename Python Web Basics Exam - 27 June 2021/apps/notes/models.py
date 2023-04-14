from django.db import models


# Create your models here.

class NoteModel(models.Model):
    title = models.CharField(
        max_length=30
    )

    image_url = models.URLField(
        verbose_name='Link to Image'
    )

    content = models.TextField()
