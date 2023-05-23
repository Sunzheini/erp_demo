from django import forms
from django.utils import translation

from erp_demo.custom_logic.custom_collections import process_numbers
from erp_demo.process_mng.models import Process, ProcessStep


PROCESS_LABELS_EN = {
    'type': 'Type',
    'number': 'Number',
    'name': 'Name',
    'process_owner': 'Process owner',
}

PROCESS_LABELS_BG = {
    'type': 'Тип',
    'number': 'Номер',
    'name': 'Име',
    'process_owner': 'Собственик',
}

PROCESS_STEP_LABELS_EN = {
    'type': 'Type',
    'number': 'Number',
    'name': 'Name',
    'parent_process': 'Parent process',
    'documents': 'Documents',
    'description': 'Description',
    'responsible': 'Responsible',
}

PROCESS_STEP_LABELS_BG = {
    'type': 'Тип',
    'number': 'Номер',
    'name': 'Име',
    'parent_process': 'Родителски процес',
    'documents': 'Документи',
    'description': 'Описание',
    'responsible': 'Отговорник',
}

PROCESS_CHOICES_BG=(
    ('Managerial', 'Управленски'),
    ('Operational', 'Оперативен'),
    ('Support', 'Поддържащ'),
)

PROCESS_STEP_CHOICES_BG=(
    ('Terminator', 'Терминатор'),
    ('Process', 'Стъпка'),
    ('Decision', 'Решение'),
)


class ProcessMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['type'].label = PROCESS_LABELS_BG['type']
            self.fields['type'].choices = PROCESS_CHOICES_BG

            self.fields['number'].label = PROCESS_LABELS_BG['number']
            self.fields['name'].label = PROCESS_LABELS_BG['name']
            self.fields['process_owner'].label = PROCESS_LABELS_BG['process_owner']


class ProcessStepMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['type'].label = PROCESS_STEP_LABELS_BG['type']
            self.fields['type'].choices = PROCESS_STEP_CHOICES_BG

            self.fields['number'].label = PROCESS_STEP_LABELS_BG['number']
            self.fields['name'].label = PROCESS_STEP_LABELS_BG['name']
            self.fields['parent_process'].label = PROCESS_STEP_LABELS_BG['parent_process']
            self.fields['documents'].label = PROCESS_STEP_LABELS_BG['documents']
            self.fields['description'].label = PROCESS_STEP_LABELS_BG['description']
            self.fields['responsible'].label = PROCESS_STEP_LABELS_BG['responsible']


class ProcessForm(forms.ModelForm, ProcessMixin):
    class Meta:
        model = Process
        fields = '__all__'

        labels = PROCESS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessStepForm(forms.ModelForm, ProcessStepMixin):
    class Meta:
        model = ProcessStep
        fields = '__all__'

        labels = PROCESS_STEP_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessEditForm(forms.ModelForm, ProcessMixin):
    class Meta:
        model = Process
        fields = '__all__'

        labels = PROCESS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessStepEditForm(forms.ModelForm, ProcessStepMixin):
    class Meta:
        model = ProcessStep
        fields = '__all__'

        labels = PROCESS_STEP_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ProcessDeleteForm(forms.ModelForm, ProcessMixin):
    class Meta:
        model = Process
        fields = '__all__'

        labels = PROCESS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class ProcessStepDeleteForm(forms.ModelForm, ProcessStepMixin):
    class Meta:
        model = ProcessStep
        fields = '__all__'

        labels = PROCESS_STEP_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translation.get_language() == 'bg':
            self.fields['process_number_dropdown'].label = 'Изберете номер на процес'
