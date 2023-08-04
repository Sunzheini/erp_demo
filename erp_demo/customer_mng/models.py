from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from cloudinary import models as cloudinary_models

from erp_demo.custom_logic.translator import translate_to_maimunica


CHOICES_EN=(
    ('', 'Empty'),
    ('Физическо лице', 'Individual'),
    ('Юридическо лице', 'Legal entity'),
    ('Институция', 'Institution'),
)


class Customer(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50
    MAX_LENGTH_PHONE = 20
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        choices=CHOICES_EN,
        blank=False, null=False,
    )

    # with cloudinary
    attachment = cloudinary_models.CloudinaryField(
        'photo',
        resource_type="auto",
        blank=True, null=True,
        use_filename=True,
        unique_filename=False,
    )

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    registration_address = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    registration_city = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    eik = models.PositiveIntegerField(
        blank=True, null=True,
    )

    mol1 = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    mol2 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    mol3 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    mol4 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    mol5 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    correspondence_address1 = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    correspondence_address2 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    correspondence_address3 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    correspondence_address4 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    correspondence_address5 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    contact_person1 = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    contact_person2 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    contact_person3 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    contact_person4 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    contact_person5 = models.CharField(
        max_length=MAX_LENGTH,
        blank=True, null=True,
    )

    phone1 = models.CharField(
        max_length=MAX_LENGTH_PHONE,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    phone2 = models.CharField(
        max_length=MAX_LENGTH_PHONE,
        blank=True, null=True,
    )

    phone3 = models.CharField(
        max_length=MAX_LENGTH_PHONE,
        blank=True, null=True,
    )

    phone4 = models.CharField(
        max_length=MAX_LENGTH_PHONE,
        blank=True, null=True,
    )

    phone5 = models.CharField(
        max_length=MAX_LENGTH_PHONE,
        blank=True, null=True,
    )

    email1 = models.EmailField(
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    email2 = models.EmailField(
        blank=True, null=True,
    )

    email3 = models.EmailField(
        blank=True, null=True,
    )

    email4 = models.EmailField(
        blank=True, null=True,
    )

    email5 = models.EmailField(
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.registration_address) < self.MIN_LENGTH:
            raise ValidationError('Registration address must be longer than 3 characters!')

        if len(self.registration_city) < self.MIN_LENGTH:
            raise ValidationError('Registration city must be longer than 3 characters!')

        if len(self.mol1) < self.MIN_LENGTH:
            raise ValidationError('MOL1 must be longer than 3 characters!')

        if len(self.correspondence_address1) < self.MIN_LENGTH:
            raise ValidationError('Correspondence address must be longer than 3 characters!')

        if len(self.contact_person1) < self.MIN_LENGTH:
            raise ValidationError('Contact person must be longer than 3 characters!')

        if len(self.phone1) < self.MIN_LENGTH:
            raise ValidationError('Phone must be longer than 3 characters!')

        if len(self.email1) < self.MIN_LENGTH:
            raise ValidationError('Email must be longer than 3 characters!')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:20])}")

        try:
            return super().save(*args, **kwargs)
        except ValidationError as v_error:
            print(f"ValidationError: {v_error}")
            raise
        except IntegrityError as i_error:
            print(f"IntegrityError: {i_error}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def __str__(self):
        return f"{self.name}"
