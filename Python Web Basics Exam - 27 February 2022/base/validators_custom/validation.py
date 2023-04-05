import re

from django.core.exceptions import ValidationError


class ValidationCustom:

    @staticmethod
    def validate_string_nums_letters_and_underscore(value):
        if not bool(re.match('^[A-Za-z0-9_-]*$', value)):
            raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')

