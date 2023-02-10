from django.db import models
from django.utils.text import slugify

from erp_demo.process_mng.models import ProcessStep


class MyTasks(models.Model):
    class Meta:
        ordering = ['id']

    number = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    description = models.TextField(
        blank=True, null=True,
    )


class CaptainsLog(models.Model):
    class Meta:
        ordering = ['id']

    operation = models.CharField(
        max_length=297,
        blank=False, null=False,
    )

    # ToDo: fix format
    performed_at_time = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    execution_time = models.CharField(
        max_length=30,
        blank=False, null=False,
    )


class Requirements(models.Model):
    class Meta:
        ordering = ['id']

    organization = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    external_document = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    clause = models.CharField(
        max_length=30,
        blank=False, null=False,
    )

    description = models.TextField(
        blank=True, null=True,
    )

    # many-to-many
    covered_by_process_step = models.ManyToManyField(
        ProcessStep,
        blank=True,
        through='RequirementToProcessStep',
        # doesn't auto create a table but uses the one specified
    )

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.organization}-{self.clause}")
        return super().save(*args, **kwargs)

    @property
    def get_related_process_steps(self):
        return RequirementToProcessStep.objects.filter(requirement_id=self.pk)

    def __str__(self):
        return f"{self.organization}-{self.clause}"


class RequirementToProcessStep(models.Model):
    requirement_id = models.ForeignKey(
        Requirements,
        on_delete=models.CASCADE,
    )
    process_step_id = models.ForeignKey(
        ProcessStep,
        on_delete=models.CASCADE,
    )
    # can also add additional info

    def __str__(self):
        return f"{self.process_step_id}"


