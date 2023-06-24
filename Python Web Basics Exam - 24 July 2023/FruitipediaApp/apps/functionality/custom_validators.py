from django.core.exceptions import ValidationError


class CustomValidators:
    @staticmethod
    def letter_start(value):
        if not value[0].isalpha():
            raise ValidationError("Your name must start with a letter!")

    @staticmethod
    def fruit_full_name_letters_only(value):
        if not value.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
