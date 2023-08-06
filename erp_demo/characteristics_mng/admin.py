from django.contrib import admin

from erp_demo.characteristics_mng.models import Characteristic


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    fields_order = ('name', 'code', 'type', 'requirement', 'attachment')
    list_display = fields_order
    list_filter = fields_order

    search_fields = ('name', 'code', 'type', 'requirement')		# only direct fields, i.e. not foreign
    ordering = ('code', 'type', 'requirement', 'name', 'attachment')
