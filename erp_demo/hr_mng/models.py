from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MinValueValidator

from erp_demo.custom_logic.translator import translate_to_maimunica


class AccessLevels(models.Model):
    MAX_LENGTH = 99

    class Meta:
        ordering = ['id']

    code = models.PositiveIntegerField(
        blank=False, null=False,
        unique=True,
    )

    description = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    def __str__(self):
        return f"{self.code} - {self.description}"


class AccessRights(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50

    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
    )

    description = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    def __str__(self):
        return f"{self.type} - {self.description}"


class Trainings(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    code = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

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

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.code) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Code must be longer than 1 character!')

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.code}-"
                           f"{self.name}")

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


class EmployeeToTrainings(models.Model):
    training_id = models.ForeignKey(
        Trainings,
        on_delete=models.CASCADE,
    )
    employee_id = models.ForeignKey(
        'Employee',     # '', since Employee is defined below
        on_delete=models.CASCADE,
    )
    # can also add additional info

    def __str__(self):
        return f"{self.training_id}"


class Positions(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 5

    class Meta:
        ordering = ['id']

    code = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
    )

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    # many-to-one
    access_rights = models.ForeignKey(
        AccessRights,                    # which is the related table
        to_field="type",
        db_column="access_right_type",
        # on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        on_delete=models.SET_NULL, null=True,   # set null when process is deleted
        # on_delete=models.RESTRICT,  # can delete if there is a process step attached
    )

    # many-to-many
    access_levels = models.ManyToManyField(
        AccessLevels,
        blank=True,
        through='PositionsToAccessLevels',
        # doesn't auto create a table but uses the one specified
    )

    def __str__(self):
        return f"{self.name}"


class PositionsToAccessLevels(models.Model):
    access_level_id = models.ForeignKey(
        AccessLevels,
        on_delete=models.CASCADE,
    )
    position_id = models.ForeignKey(
        Positions,
        on_delete=models.CASCADE,
    )
    # can also add additional info

    def __str__(self):
        return f"{self.position_id}"


class Employee(models.Model):
    MAX_LENGTH_SHORT = 50
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1
    MIN_SHORT_LENGTH_EGN = 10

    class Meta:
        ordering = ['id']

    # # many-to-one
    position = models.ForeignKey(
        Positions,                    # which is the related table
        to_field="code",
        db_column="position_code",
        # on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        on_delete=models.SET_NULL, null=True,   # set null when process is deleted
        # on_delete=models.RESTRICT,  # can delete if there is a process step attached
    )

    contract_number = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    starting_date = models.DateField(
        blank=True, null=True,
    )

    date_last_hse_training = models.DateField(
        blank=True, null=True,
    )

    date_next_hse_training = models.DateField(
        blank=True, null=True,
    )

    egn = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH_EGN),
        ),
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    middle_name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    identification = models.PositiveIntegerField(
        blank=False, null=False,
        unique=True,
        validators=(
            MinValueValidator(1),
        )
    )

    # many-to-many
    trainings = models.ManyToManyField(
        Trainings,
        blank=True,
        through='EmployeeToTrainings',
        # doesn't auto create a table but uses the one specified
    )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def clean(self):
        if len(self.first_name) < self.MIN_LENGTH:
            raise ValidationError('First Name must be longer than 3 characters!')

        if len(self.middle_name) < self.MIN_LENGTH:
            raise ValidationError('Middle Name must be longer than 3 characters!')

        if len(self.last_name) < self.MIN_LENGTH:
            raise ValidationError('Last Name must be longer than 3 characters!')

        if len(self.egn) < self.MIN_SHORT_LENGTH_EGN:
            raise ValidationError('EGN must be longer than 10 characters!')

        if self.identification < 1:
            raise ValidationError('Identification must be greater than 0!')

        if len(self.contract_number) < self.MIN_LENGTH:
            raise ValidationError('Contract Number must be longer than 1 character!')

    @property
    def get_related_trainings(self):
        # return ', '.join([str(f) for f in EmployeeToTrainings.objects.filter(employee_id=self.pk)])
        # return ', '.join([str(f) for f in ProcessStepToDocuments.objects.filter(process_step_id=self.pk)])
        try:
            result = EmployeeToTrainings.objects.filter(employee_id=self.pk)
        except EmployeeToTrainings.DoesNotExist:
            result = None
        return result

    @property
    def name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    @property
    def name_and_position(self):
        return f"{self.get_full_name}, {self.position}"

    def __str__(self):
        return f"{self.get_full_name}, " \
               f"{self.identification}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.identification}-"
                                f"{translate_to_maimunica(self.first_name)}-"
                                f"{translate_to_maimunica(self.last_name)}")

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
