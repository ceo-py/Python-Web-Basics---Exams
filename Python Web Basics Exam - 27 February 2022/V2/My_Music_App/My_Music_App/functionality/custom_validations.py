from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

username_validator = RegexValidator(
    r'[a-zA-Z0-9_]+',
    'Ensure this value contains only letters, numbers, and underscore.',
)


def validate_username_re(value):
    return re.match(r'^[a-zA-Z0-9_]+$', value)


def validate_username(value):
    if not bool(validate_username_re(value)):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')

