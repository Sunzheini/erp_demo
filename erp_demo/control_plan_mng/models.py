from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.utils.text import slugify
from django.core.validators import MinLengthValidator

from erp_demo.characteristics_mng.models import Characteristic
from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.calibration_mng.models import MeasuringEquipment
from erp_demo.dox_mng.models import Document
from erp_demo.hr_mng.models import Employee
from erp_demo.maintenance_mng.models import Machine

control_plan_type_choices = [
    ('Prototype', 'Prototype'),
    ('Pre-launch', 'Pre-launch'),
    ('Production', 'Production'),
]


class ProcessControlPlanStep(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50
    MIN_LENGTH = 3

    class Meta:
        ordering = ['id']

    # Process Name / Operation Description
    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    machines = models.ManyToManyField(
        Machine,
        related_name='machines',
        blank=True,
        through='ProcessControlPlanStepToMachine',
    )

    characteristics = models.ManyToManyField(
        Characteristic,
        related_name='characteristic',
        blank=True,
        through='ProcessControlPlanStepToCharacteristic',
    )

    measuring_equipment = models.ManyToManyField(
        MeasuringEquipment,
        related_name='measuring_equipment',
        blank=True,
        through='ProcessControlPlanStepToMeasuringEquipment',
    )

    sample_size = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=True,
        null=True,
    )

    frequency = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=True,
        null=True,
    )

    documents = models.ManyToManyField(
        Document,
        blank=True,
        through='ProcessControlPlanStepToDocuments',
        # doesn't auto create a table but uses the one specified
    )

    reaction_plan = models.TextField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

    @property
    def get_related_machines(self):
        try:
            result = ProcessControlPlanStepToMachine.objects.filter(process_control_plan_step_id=self.pk)
        except ProcessControlPlanStepToMachine.DoesNotExist:
            result = None
        return result

    @property
    def get_related_characteristics(self):
        try:
            result = ProcessControlPlanStepToCharacteristic.objects.filter(process_control_plan_step_id=self.pk)
        except ProcessControlPlanStepToCharacteristic.DoesNotExist:
            result = None
        return result

    @property
    def get_related_product_characteristics(self):
        try:
            result = ProcessControlPlanStepToCharacteristic.objects.filter(
                process_control_plan_step_id=self.pk, characteristic__type='Product'
            )
        except ProcessControlPlanStepToCharacteristic.DoesNotExist:
            result = None
        return result

    @property
    def get_related_process_characteristics(self):
        try:
            result = ProcessControlPlanStepToCharacteristic.objects.filter(
                process_control_plan_step_id=self.pk, characteristic__type='Process'
            )
        except ProcessControlPlanStepToCharacteristic.DoesNotExist:
            result = None
        return result

    @property
    def get_related_measuring_equipment(self):
        try:
            result = ProcessControlPlanStepToMeasuringEquipment.objects.filter(process_control_plan_step_id=self.pk)
        except ProcessControlPlanStepToMeasuringEquipment.DoesNotExist:
            result = None
        return result

    @property
    def get_related_documents(self):
        try:
            result = ProcessControlPlanStepToDocuments.objects.filter(process_control_plan_step_id=self.pk)
        except ProcessControlPlanStepToDocuments.DoesNotExist:
            result = None
        return result

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

    def __str__(self):
        return f"{self.name}"


# will be the same as Process in the process app
class ProcessControlPlan(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 50
    MIN_LENGTH = 3
    MIN_SHORT_LENGTH = 1

    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False,
        null=False,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    type = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False,
        null=False,
        choices=control_plan_type_choices,
    )

    number = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    revision = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_SHORT_LENGTH),
        ),
    )

    creation_date = models.DateField(
        blank=False,
        null=False,
        auto_now_add=True,
    )

    update_date = models.DateField(
        blank=False,
        null=False,
        auto_now=True,
    )

    product = models.CharField(
        max_length=MAX_LENGTH,
        blank=False,
        null=False,
        validators=(
            MinLengthValidator(MIN_LENGTH),
        ),
    )

    owner = models.ForeignKey(
        Employee,
        blank=True,
        to_field='id',
        db_column="employee_id",
        # on_delete=models.CASCADE,
        on_delete=models.SET_NULL, null=True,
    )

    team = models.TextField(
        blank=True,
        null=True,
    )

    steps = models.ManyToManyField(
        ProcessControlPlanStep,
        blank=True,
        through='ProcessControlPlanToProcessControlPlanStep',
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def clean(self):
        if len(self.name) < self.MIN_LENGTH:
            raise ValidationError('Name must be longer than 3 characters!')

        if len(self.number) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Number must be longer than 1 character!')

        if len(self.revision) < self.MIN_SHORT_LENGTH:
            raise ValidationError('Revision must be longer than 1 character!')

        if len(self.product) < self.MIN_LENGTH:
            raise ValidationError('Product must be longer than 3 characters!')

    @property
    def list_of_characteristic_types(self):
        return [x[0] for x in self._meta.get_field('type').choices]

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

    def __str__(self):
        return f"{self.name}"


class ProcessControlPlanStepToMachine(models.Model):
    process_control_plan_step_id = models.ForeignKey(
        ProcessControlPlanStep,
        on_delete=models.CASCADE,
    )

    machine_id = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.machine_id}"


class ProcessControlPlanStepToCharacteristic(models.Model):
    process_control_plan_step_id = models.ForeignKey(
        ProcessControlPlanStep,
        on_delete=models.CASCADE,
    )

    characteristic_id = models.ForeignKey(
        Characteristic,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.characteristic_id}"


class ProcessControlPlanStepToMeasuringEquipment(models.Model):
    process_control_plan_step_id = models.ForeignKey(
        ProcessControlPlanStep,
        on_delete=models.CASCADE,
    )

    measuring_equipment_id = models.ForeignKey(
        MeasuringEquipment,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.measuring_equipment_id}"


class ProcessControlPlanStepToDocuments(models.Model):
    process_control_plan_step_id = models.ForeignKey(
        ProcessControlPlanStep,
        on_delete=models.CASCADE,
    )

    document_id = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.document_id}"


class ProcessControlPlanToProcessControlPlanStep(models.Model):
    process_control_plan_id = models.ForeignKey(
        ProcessControlPlan,
        on_delete=models.CASCADE,
    )

    process_control_plan_step_id = models.ForeignKey(
        ProcessControlPlanStep,
        on_delete=models.CASCADE,
    )
