from django import forms
from django.utils import translation

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
