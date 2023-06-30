from django.db import models

# Create your models here.

class ProfileModel(models.Model):

    first_name = models.CharField(
        max_length=30,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=30,
        verbose_name='Last Name'
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
