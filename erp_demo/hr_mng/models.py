from django.db import models
from django.utils.text import slugify


class AccessLevels(models.Model):
    class Meta:
        ordering = ['id']

    code = models.PositiveIntegerField(
        blank=False, null=False,
        unique=True,
    )

    description = models.CharField(
        max_length=70,
        blank=False, null=False,
    )


class AccessRights(models.Model):
    class Meta:
        ordering = ['id']

    type = models.CharField(
        max_length=30,
        blank=False, null=False,
        unique=True,
    )

    description = models.CharField(
        max_length=70,
        blank=False, null=False,
    )


class Trainings(models.Model):
    class Meta:
        ordering = ['id']

    code = models.CharField(
        max_length=30,
        blank=False, null=False,
        unique=True,
    )

    name = models.CharField(
        max_length=50,
        blank=False, null=False,
    )

    description = models.TextField(
        blank=True, null=True,
    )

    slug = models.SlugField(
        blank=True, null=True, editable=False,
    )

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.code}")
        return super().save(*args, **kwargs)


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
    class Meta:
        ordering = ['id']

    code = models.CharField(
        max_length=5,
        blank=False, null=False,
        unique=True,
    )

    name = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    # many-to-one
    access_rights = models.ForeignKey(
        AccessRights,                    # which is the related table
        to_field="type",
        db_column="access_right_type",
        on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        # on_delete=models.SET_NULL, null=True,   # set null when process is deleted
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
        return f"{self.code}"


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
    class Meta:
        ordering = ['id']

    # # many-to-one
    position = models.ForeignKey(
        Positions,                    # which is the related table
        to_field="code",
        db_column="position_code",
        on_delete=models.CASCADE,   # when process is deleted, delete related process steps
        # on_delete=models.SET_NULL, null=True,   # set null when process is deleted
        # on_delete=models.RESTRICT,  # can delete if there is a process step attached
    )

    contract_number = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    # starting_date = models.CharField(
    #     max_length=30,
    #     blank=False, null=False,
    # )

    # ToDo: fix to DateTime or similar field
    starting_date = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    date_last_hse_training = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    date_next_hse_training = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    egn = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    first_name = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    middle_name = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    last_name = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    identification = models.PositiveIntegerField(
        blank=False, null=False,
        unique=True,
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

    @property
    def get_related_trainings(self):
        return ', '.join([str(f) for f in EmployeeToTrainings.objects.filter(employee_id=self.pk)])

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name}, " \
               f"{self.identification}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            # self.slug = slugify(f"{self.get_full_name}")
            self.slug = slugify(f"{self.identification}-{self.position}")
        return super().save(*args, **kwargs)
