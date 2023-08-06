from django.contrib import admin

from erp_demo.control_plan_mng.models import ProcessControlPlanStep, ProcessControlPlan


@admin.register(ProcessControlPlan)
class ProcessControlPlanAdmin(admin.ModelAdmin):
    fields_order = ('name', 'type', 'number', 'revision',
                    'creation_date', 'update_date', 'product', 'owner', 'team', 'steps')
    list_display = ('name', 'type', 'number', 'revision',
                    'creation_date', 'update_date', 'product', 'owner', 'team')
    list_filter = fields_order

    list_select_related = ('owner',) 	# Optimize ForeignKey lookups in list view

    search_fields = ('name', 'type', 'number', 'revision',
                    'creation_date', 'update_date', 'product', 'team')	# only direct fields, i.e. not foreign
    ordering = ('owner', 'name', 'type', 'number', 'revision')


@admin.register(ProcessControlPlanStep)
class ProcessControlPlanStepAdmin(admin.ModelAdmin):
    fields_order = ('name', 'machines', 'characteristics',
                    'measuring_equipment', 'sample_size', 'frequency', 'documents', 'reaction_plan')
    list_display = ('name', 'sample_size', 'frequency', 'reaction_plan')
    list_filter = fields_order

    list_select_related = []

    search_fields = ('name', 'sample_size', 'frequency')		# only direct fields, i.e. not foreign
    ordering = ('name', 'sample_size', 'frequency')
