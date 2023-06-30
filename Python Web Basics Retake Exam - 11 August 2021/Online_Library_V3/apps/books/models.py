from django.db import models

# Create your models here.
class BooksModel(models.Model):

    title = models.CharField(
        max_length=30,
        verbose_name='Title'
    )

    description = models.CharField(
        verbose_name='Description',
    )

    image = models.URLField(
        verbose_name='Image',
    )

    type = models.CharField(
        max_length=30,
        verbose_name='Type'
    )

    def book_title(self):
        return f'{self.title if len(self.title) < 18 else self.title[:18] + "..."}'
