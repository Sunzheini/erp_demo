from django.db import models
from django.utils.text import slugify

from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.hr_mng.models import Positions
from erp_demo.maintenance_mng.models import Machine
from erp_demo.supplier_mng.models import Material


class Analysis(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(
        max_length=199,
        blank=False,
        null=False,
        unique=True,
    )

    code = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        unique=True,
    )

    measurement_unit = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )

    # materials = models.ManyToManyField(Material, blank=True)
    #
    # work_force = models.ManyToManyField(Positions, blank=True)
    #
    # machines = models.ManyToManyField(Machine, blank=True)

    # -------------------------------------------------------------------------
    material1 = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='material1',
    )

    material2 = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='material2',
    )

    material3 = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='material3',
    )

    material4 = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='material4',
    )

    material5 = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='material5',
    )

    position1 = models.ForeignKey(
        Positions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='position1',
    )

    position2 = models.ForeignKey(
        Positions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='position2',
    )

    position3 = models.ForeignKey(
        Positions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='position3',
    )

    position4 = models.ForeignKey(
        Positions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='position4',
    )

    position5 = models.ForeignKey(
        Positions,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='position5',
    )

    machine1 = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='machine1',
    )

    machine2 = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='machine2',
    )

    machine3 = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='machine3',
    )

    machine4 = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='machine4',
    )

    machine5 = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='machine5',
    )

    # -------------------------------------------------------------------------

    material1_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    material2_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    material3_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    material4_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    material5_measurement_unit = models.CharField(max_length=50, blank=True, null=True)

    position1_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    position2_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    position3_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    position4_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    position5_measurement_unit = models.CharField(max_length=50, blank=True, null=True)

    machine1_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    machine2_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    machine3_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    machine4_measurement_unit = models.CharField(max_length=50, blank=True, null=True)
    machine5_measurement_unit = models.CharField(max_length=50, blank=True, null=True)

    # -------------------------------------------------------------------------

    material1_cost_rate = models.FloatField(blank=True, null=True)
    material2_cost_rate = models.FloatField(blank=True, null=True)
    material3_cost_rate = models.FloatField(blank=True, null=True)
    material4_cost_rate = models.FloatField(blank=True, null=True)
    material5_cost_rate = models.FloatField(blank=True, null=True)

    position1_cost_rate = models.FloatField(blank=True, null=True)
    position2_cost_rate = models.FloatField(blank=True, null=True)
    position3_cost_rate = models.FloatField(blank=True, null=True)
    position4_cost_rate = models.FloatField(blank=True, null=True)
    position5_cost_rate = models.FloatField(blank=True, null=True)

    machine1_cost_rate = models.FloatField(blank=True, null=True)
    machine2_cost_rate = models.FloatField(blank=True, null=True)
    machine3_cost_rate = models.FloatField(blank=True, null=True)
    machine4_cost_rate = models.FloatField(blank=True, null=True)
    machine5_cost_rate = models.FloatField(blank=True, null=True)

    # -------------------------------------------------------------------------

    material1_price = models.FloatField(blank=True, null=True)
    material2_price = models.FloatField(blank=True, null=True)
    material3_price = models.FloatField(blank=True, null=True)
    material4_price = models.FloatField(blank=True, null=True)
    material5_price = models.FloatField(blank=True, null=True)

    position1_price = models.FloatField(blank=True, null=True)
    position2_price = models.FloatField(blank=True, null=True)
    position3_price = models.FloatField(blank=True, null=True)
    position4_price = models.FloatField(blank=True, null=True)
    position5_price = models.FloatField(blank=True, null=True)

    machine1_price = models.FloatField(blank=True, null=True)
    machine2_price = models.FloatField(blank=True, null=True)
    machine3_price = models.FloatField(blank=True, null=True)
    machine4_price = models.FloatField(blank=True, null=True)
    machine5_price = models.FloatField(blank=True, null=True)

    # -------------------------------------------------------------------------

    @property
    def material1_total(self):
        if self.material1_cost_rate and self.material1_price:
            return self.material1_cost_rate * self.material1_price
        else:
            return 0

    @property
    def material2_total(self):
        if self.material2_cost_rate and self.material2_price:
            return self.material2_cost_rate * self.material2_price
        else:
            return 0

    @property
    def material3_total(self):
        if self.material3_cost_rate and self.material3_price:
            return self.material3_cost_rate * self.material3_price
        else:
            return 0

    @property
    def material4_total(self):
        if self.material4_cost_rate and self.material4_price:
            return self.material4_cost_rate * self.material4_price
        else:
            return 0

    @property
    def material5_total(self):
        if self.material5_cost_rate and self.material5_price:
            return self.material5_cost_rate * self.material5_price
        else:
            return 0

    @property
    def position1_total(self):
        if self.position1_cost_rate and self.position1_price:
            return self.position1_cost_rate * self.position1_price
        else:
            return 0

    @property
    def position2_total(self):
        if self.position2_cost_rate and self.position2_price:
            return self.position2_cost_rate * self.position2_price
        else:
            return 0

    @property
    def position3_total(self):
        if self.position3_cost_rate and self.position3_price:
            return self.position3_cost_rate * self.position3_price
        else:
            return 0

    @property
    def position4_total(self):
        if self.position4_cost_rate and self.position4_price:
            return self.position4_cost_rate * self.position4_price
        else:
            return 0

    @property
    def position5_total(self):
        if self.position5_cost_rate and self.position5_price:
            return self.position5_cost_rate * self.position5_price
        else:
            return 0

    @property
    def machine1_total(self):
        if self.machine1_cost_rate and self.machine1_price:
            return self.machine1_cost_rate * self.machine1_price
        else:
            return 0

    @property
    def machine2_total(self):
        if self.machine2_cost_rate and self.machine2_price:
            return self.machine2_cost_rate * self.machine2_price
        else:
            return 0

    @property
    def machine3_total(self):
        if self.machine3_cost_rate and self.machine3_price:
            return self.machine3_cost_rate * self.machine3_price
        else:
            return 0

    @property
    def machine4_total(self):
        if self.machine4_cost_rate and self.machine4_price:
            return self.machine4_cost_rate * self.machine4_price
        else:
            return 0

    @property
    def machine5_total(self):
        if self.machine5_cost_rate and self.machine5_price:
            return self.machine5_cost_rate * self.machine5_price
        else:
            return 0

    # -------------------------------------------------------------------------
    @property
    def total_materials_cost(self):
        return self.material1_total + self.material2_total + self.material3_total + self.material4_total + self.material5_total

    @property
    def total_positions_cost(self):
        return self.position1_total + self.position2_total + self.position3_total + self.position4_total + self.position5_total

    @property
    def total_machines_cost(self):
        return self.machine1_total + self.machine2_total + self.machine3_total + self.machine4_total + self.machine5_total

    # -------------------------------------------------------------------------

    additional_expense_materials_cost_rate = models.FloatField(blank=True, null=True)
    additional_expense_positions_cost_rate = models.FloatField(blank=True, null=True)
    additional_expense_machines_cost_rate = models.FloatField(blank=True, null=True)

    @property
    def additional_expense_materials_total(self):
        if self.additional_expense_materials_cost_rate:
            return self.additional_expense_materials_cost_rate * self.total_materials_cost
        else:
            return 0

    @property
    def additional_expense_positions_total(self):
        if self.additional_expense_positions_cost_rate:
            return self.additional_expense_positions_cost_rate * self.total_positions_cost
        else:
            return 0

    @property
    def additional_expense_machines_total(self):
        if self.additional_expense_machines_cost_rate:
            return self.additional_expense_machines_cost_rate * self.total_machines_cost
        else:
            return 0

    # -------------------------------------------------------------------------

    @property
    def total_direct_costs(self):
        return self.total_materials_cost + self.total_positions_cost + self.total_machines_cost

    @property
    def total_additional_costs(self):
        return self.additional_expense_materials_total + self.additional_expense_positions_total + self.additional_expense_machines_total

    # -------------------------------------------------------------------------

    @property
    def total_costs(self):
        return self.total_direct_costs + self.total_additional_costs

    profit = models.FloatField(blank=True, null=True)

    @property
    def final_price(self):
        return self.total_costs * (1 + self.profit / 100)

    # -------------------------------------------------------------------------

    slug = models.SlugField(
        blank=True, null=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{translate_to_maimunica(self.name[0:30])}")

        return super().save(*args, **kwargs)
