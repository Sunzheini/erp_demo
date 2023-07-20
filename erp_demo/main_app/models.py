from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.process_mng.models import ProcessStep


class MyTasks(models.Model):
    MAX_LENGTH = 99

    class Meta:
        ordering = ['id']

    number = models.CharField(
        max_length=MAX_LENGTH,
        blank=False, null=False,
    )

    description = models.TextField(
        blank=True, null=True,
    )


class CaptainsLog(models.Model):
    MAX_LENGTH_LONG = 297
    MAX_LENGTH_SHORT = 30

    class Meta:
        ordering = ['id']

    operation = models.CharField(
        max_length=MAX_LENGTH_LONG,
        blank=False, null=False,
    )

    performed_at_time = models.DateTimeField(
        blank=False, null=False,
        auto_now_add=True,
    )

    execution_time = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
    )


class Requirements(models.Model):
    MAX_LENGTH = 99
    MAX_LENGTH_SHORT = 30

    class Meta:
        ordering = ['id']

    organization = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
    )

    external_document = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
    )

    clause = models.CharField(
        max_length=MAX_LENGTH_SHORT,
        blank=False, null=False,
    )

    clause_name = models.CharField(
        max_length=MAX_LENGTH,
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
        # super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.organization}-"
                                f"{self.clause}-"
                                f"{translate_to_maimunica(self.description[0:20])}")
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


