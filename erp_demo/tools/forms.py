from django import forms
from django.utils import translation

from erp_demo.control_plan_mng.forms import PROCESS_CONTROL_PLAN_NAME_LABELS_BG, PROCESS_CONTROL_PLAN_NAME_LABELS_EN
from erp_demo.control_plan_mng.models import ProcessControlPlan
from erp_demo.custom_logic.custom_collections import process_numbers


class AuditProcessNumberForm(forms.Form):
    PROCESS_NUMBERS = process_numbers

    process_number_dropdown = forms.ChoiceField(
        label='Select process number',
        choices=PROCESS_NUMBERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translation.get_language() == 'bg':
            self.fields['process_number_dropdown'].label = 'Изберете номер на процес'


class AuditProcessControlPlanNameForm(forms.Form):
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['process_control_plan'].label = PROCESS_CONTROL_PLAN_NAME_LABELS_BG['name']

    process_control_plan = forms.ChoiceField(
        label=PROCESS_CONTROL_PLAN_NAME_LABELS_EN['name'],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['process_control_plan'].choices = [(pcp.id, pcp.name) for pcp in ProcessControlPlan.objects.all()]
        self.change_labels_to_bg()
