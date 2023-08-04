from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.hr_mng.models import Employee
from erp_demo.custom_logic.translator import translate_to_maimunica


STATUS_CHOICES_EN = (
    ('Not Started', 'Not Started'),
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
)


class NewAction(models.Model):
    MAX_LENGTH_SHORT = 50
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    scope = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=True, null=True,
    )

    # description of the action itself
    name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    # # many-to-one
    responsible = models.ForeignKey(
        Employee,
        to_field="identification",
        db_column="owner_ident",
        # on_delete=models.CASCADE,
        on_delete=models.SET_NULL, null=True,
        related_name="responsible",
    )

    target_date = models.DateField(
        blank=False, null=False,
    )

    comments = models.TextField(
        blank=True, null=True,
    )

    status = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        choices=STATUS_CHOICES_EN,
        blank=False, null=False,
    )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")

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
