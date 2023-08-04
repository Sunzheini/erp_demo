from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.hr_mng.models import Employee
from erp_demo.process_mng.models import Process


class Resource(models.Model):
    MAX_LENGTH = 99
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    description = models.TextField(
        blank=True, null=True,
    )

    quantity = models.PositiveIntegerField(
        blank=False, null=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def assigned_quantity(self):
        return sum(
            [assigned_resource.quantity for assigned_resource in ResourcesAssignedToEmployees.objects.filter(resource=self)]
            ) + sum(
            [assigned_resource.quantity for assigned_resource in ResourcesAssignedToProcess.objects.filter(resource=self)]
            )

    @property
    def available_quantity(self):
        return self.quantity - self.assigned_quantity

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

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


class ResourcesAssignedToEmployees(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']
        unique_together = [['resource', 'employee']]


class ResourcesAssignedToProcess(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']
        unique_together = [['resource', 'process']]
