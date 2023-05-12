from django import forms

from erp_demo.custom_logic.custom_collections import process_numbers
from erp_demo.process_mng.models import Process, ProcessStep


class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'


class ProcessStepForm(forms.ModelForm):
    class Meta:
        model = ProcessStep
        fields = '__all__'


class ProcessEditForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'


class ProcessStepEditForm(forms.ModelForm):
    class Meta:
        model = ProcessStep
        fields = '__all__'


class ProcessDeleteForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class ProcessStepDeleteForm(forms.ModelForm):
    class Meta:
        model = ProcessStep
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class ProcessNumberForm(forms.Form):
    PROCESS_NUMBERS = process_numbers

    process_number_dropdown = forms.ChoiceField(
        label='Select process number',
        choices=PROCESS_NUMBERS,
    )
