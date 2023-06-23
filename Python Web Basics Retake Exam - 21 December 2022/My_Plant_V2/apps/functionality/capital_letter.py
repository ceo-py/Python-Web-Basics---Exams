from django.core.exceptions import ValidationError


def validate_user_name(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def validate_plant_name(value):
    if not value[0].isupper():
        raise ValidationError("Plant name should contain only letters!")