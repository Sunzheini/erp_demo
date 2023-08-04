from django.contrib.auth.models import AbstractUser
from django.core import validators

from django.db import models


class AppUser(AbstractUser):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_NAME_LENGTH),
        )
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_NAME_LENGTH),
        )
    )
    email = models.EmailField(
        unique=True,
    )

    def get_first_letter(self):
        return self.username[0].upper()
