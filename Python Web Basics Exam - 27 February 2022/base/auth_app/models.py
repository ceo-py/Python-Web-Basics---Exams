from django.core import validators
from django.db import models
from base.validators_custom.validation import ValidationCustom as vc


class ProfileModel(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=(
            validators.MinLengthValidator(2),
            vc.validate_string_nums_letters_and_underscore,
        ),
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=True, null=True, validators=(validators.MinValueValidator(0),)
    )
