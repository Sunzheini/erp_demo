from django.contrib import admin

from erp_demo.calibration_mng.models import MeasuringEquipment


@admin.register(MeasuringEquipment)
class MeasuringEquipmentAdmin(admin.ModelAdmin):
    fields_order = ('name', 'inventory_number', 'characteristics', 'installation_date', 'calibration_interval_in_days')
    list_display = fields_order
    list_filter = fields_order

    search_fields = fields_order		# only direct fields, i.e. not foreign
    ordering = ('installation_date', 'calibration_interval_in_days', 'name', 'inventory_number', 'characteristics', )