from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.hr_mng.models import Employee
from erp_demo.newactions_mng.models import NewAction


class ActionPlan(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
        unique=True,
    )

    description = models.TextField(
        blank=True, null=True,
    )

    owner = models.ForeignKey(
        Employee,
        to_field='id',
        db_column="employee_id",
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    @property
    def get_all_steps(self):
        return ActionPlanStep.objects.filter(parent_action_plan_id=self.pk)

    @property
    def count_all_steps(self):
        return ActionPlanStep.objects.filter(parent_action_plan_id=self.pk).count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class ActionPlanStep(models.Model):
    class Meta:
        ordering = ['number']

    number = models.PositiveIntegerField(
        blank=False, null=False,
    )

    scope = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    # Open Issue
    name = models.CharField(
        max_length=99,
        blank=False, null=False,
        unique=True,
    )

    # many-to-one
    parent_action_plan = models.ForeignKey(
        ActionPlan,
        to_field="id",
        db_column="parent_action_plan_id",
        on_delete=models.CASCADE,
    )

    actions = models.ManyToManyField(
        NewAction,
        related_name='actions',
        blank=True,
        through='ActionPlanStepToActions',
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    @property
    def get_related_actions(self):
        return ActionPlanStepToActions.objects.filter(action_plan_step_id=self.pk)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class ActionPlanStepToActions(models.Model):
    action_plan_step_id = models.ForeignKey(
        ActionPlanStep,
        on_delete=models.CASCADE,
    )
    action_id = models.ForeignKey(
        NewAction,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.action_id}"
