from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.customer_mng.models import Customer
from erp_demo.hr_mng.models import Employee


class Nonconformity(models.Model):
    class Meta:
        ordering = ['id']

# general info
# -----------------------------------------------------------------------------

    # many to one
    customer = models.ForeignKey(
        Customer,
        to_field='id',
        db_column="customer_id",
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    customer_claim_number = models.CharField(
        max_length=50,
        blank=True, null=True,
    )

    customer_claim_date = models.DateField(
        blank=True, null=True,
    )

    internal_claim_number = models.CharField(
        max_length=50,
        blank=True, null=True,
    )

    nonconformity_start_date = models.DateField(
        blank=True, null=True,
    )

    part_number = models.CharField(
        max_length=50,
        blank=True, null=True,
    )

    part_revision = models.CharField(
        max_length=50,
        blank=True, null=True,
    )

    part_name = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

# D1 - Problem Definition
# -----------------------------------------------------------------------------

    name = models.CharField(
        max_length=99,
        blank=False, null=False,
    )

    internal_definition = models.TextField(
        blank=True, null=True,
    )

# D2 - Form a team
# -----------------------------------------------------------------------------

    # many to one
    nonconformity_owner = models.ForeignKey(
        Employee,
        to_field='id',
        db_column="employee_id",
        on_delete=models.CASCADE,
        blank=True, null=True,
    )

    team_members = models.TextField(
        blank=True, null=True,
    )

# D3 - Short Term (Containment and Correction) Actions
# -----------------------------------------------------------------------------

    containment_actions = models.TextField(
        blank=True, null=True,
    )

    correction_actions = models.TextField(
        blank=True, null=True,
    )

# D4 - Root Cause Analysis
# -----------------------------------------------------------------------------

    possible_root_cause1 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause1_ask_why1 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause1_ask_why2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause1_ask_why3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause1_ask_why4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause1_ask_why5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    possible_root_cause2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause2_ask_why1 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause2_ask_why2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause2_ask_why3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause2_ask_why4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause2_ask_why5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    possible_root_cause3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause3_ask_why1 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause3_ask_why2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause3_ask_why3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause3_ask_why4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause3_ask_why5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    possible_root_cause4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause4_ask_why1 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause4_ask_why2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause4_ask_why3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause4_ask_why4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause4_ask_why5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    possible_root_cause5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause5_ask_why1 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause5_ask_why2 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause5_ask_why3 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause5_ask_why4 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    cause5_ask_why5 = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

# D5 - D7 - Define, Implement and Verify the effectiveness of Permanent Corrective Actions
# -----------------------------------------------------------------------------

    permanent_corrective_actions = models.TextField(
        blank=True, null=True,
    )

    breakpoint_batch_number = models.CharField(
        max_length=99,
        blank=True, null=True,
    )

    breakpoint_at_customer_date = models.DateField(
        blank=True, null=True,
    )

# D8 - Systematic actions to prevent recurrence
# -----------------------------------------------------------------------------

    systematic_actions = models.TextField(
        blank=True, null=True,
    )

# -----------------------------------------------------------------------------

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"