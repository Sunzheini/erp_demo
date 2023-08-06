from django.contrib import admin

from erp_demo.actionplan_mng.models import ActionPlan, ActionPlanStep


@admin.register(ActionPlan)
class ActionPlanAdmin(admin.ModelAdmin):
    fields_order = ('name', 'description', 'owner')
    list_display = fields_order
    list_filter = fields_order

    list_select_related = ('owner',)  # Optimize ForeignKey lookups in list view

    search_fields = ('name', 'description')		# only direct fields, i.e. not foreign
    ordering = ('owner', 'name', 'description')


@admin.register(ActionPlanStep)
class ActionPlanStepAdmin(admin.ModelAdmin):
    fields_order = ('number', 'scope', 'name', 'parent_action_plan', 'actions')
    list_display = fields_order
    list_filter = fields_order

    list_select_related = ('parent_action_plan',)  # Optimize ForeignKey lookups in list view

    search_fields = ('number', 'scope', 'name')		# only direct fields, i.e. not foreign
    ordering = ('parent_action_plan', 'number', 'scope', 'name', 'actions')
