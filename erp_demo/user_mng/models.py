from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
#
# from erp_demo.user_mng.managers import AppUserManager
#
#
# class AppUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(
#         unique=True,
#         null=False,
#         blank=False,
#     )
#     date_joined = models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     is_staff = models.BooleanField(
#         default=False,
#         null=False,
#         blank=False,
#     )
#
#     # user credentials consist of email and password
#     USERNAME_FIELD = 'email'
#
#     object = AppUserManager()
#
#
# class Profile(models.Model):
#     first_name = models.CharField(
#         max_length=25,
#     )
#
#     last_name = models.CharField(
#         max_length=25,
#     )
#
#     age = models.PositiveIntegerField()
#
#     user = models.OneToOneField(
#         AppUser,
#         primary_key=True,
#         on_delete=models.CASCADE,
#     )
#


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
