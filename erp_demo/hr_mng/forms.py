import os
from django import forms
from django.utils import translation

from erp_demo.hr_mng.models import Employee, Trainings


EMPLOYEE_LABELS_EN = {
    'position': 'Position',
    'contract_number': 'Contract number',
    'starting_date': 'Starting date',
    'date_last_hse_training': 'Date last HSE training',
    'date_next_hse_training': 'Date next HSE training',
    'egn': 'Egn',
    'first_name': 'First name',
    'middle_name': 'Middle name',
    'last_name': 'Last name',
    'identification': 'Identification',
    'trainings': 'Trainings',
}

EMPLOYEE_LABELS_BG = {
    'position': 'Длъжност',
    'contract_number': 'Номер на договор',
    'starting_date': 'Назначен на',
    'date_last_hse_training': 'Последно HSE обуч.',
    'date_next_hse_training': 'Следващо HSE обуч.',
    'egn': 'ЕГН',
    'first_name': 'Име',
    'middle_name': 'Презиме',
    'last_name': 'Фамилия',
    'identification': 'Идентификация',
    'trainings': 'Обучения',
}

TRAINING_LABELS_EN = {
    'code': 'Code',
    'name': 'Name',
    'description': 'Description',
}

TRAINING_LABELS_BG = {
    'code': 'Код',
    'name': 'Име',
    'description': 'Описание',
}

class EmployeeModelAndExcludeMixin:
    class Meta:
        model = Employee
        exclude = ['slug']

        widgets = {
            'starting_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',  # taka veshe izkarva kalendara
                }
            ),
            'date_last_hse_training': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'date_next_hse_training': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['position'].label = EMPLOYEE_LABELS_BG['position']
            self.fields['contract_number'].label = EMPLOYEE_LABELS_BG['contract_number']
            self.fields['starting_date'].label = EMPLOYEE_LABELS_BG['starting_date']
            self.fields['date_last_hse_training'].label = EMPLOYEE_LABELS_BG['date_last_hse_training']
            self.fields['date_next_hse_training'].label = EMPLOYEE_LABELS_BG['date_next_hse_training']
            self.fields['egn'].label = EMPLOYEE_LABELS_BG['egn']
            self.fields['first_name'].label = EMPLOYEE_LABELS_BG['first_name']
            self.fields['middle_name'].label = EMPLOYEE_LABELS_BG['middle_name']
            self.fields['last_name'].label = EMPLOYEE_LABELS_BG['last_name']
            self.fields['identification'].label = EMPLOYEE_LABELS_BG['identification']
            self.fields['trainings'].label = EMPLOYEE_LABELS_BG['trainings']


class TrainingsModelAndExcludeMixin:
    class Meta:
        model = Trainings
        exclude = ['slug']

    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['code'].label = TRAINING_LABELS_BG['code']
            self.fields['name'].label = TRAINING_LABELS_BG['name']
            self.fields['description'].label = TRAINING_LABELS_BG['description']

# ----------------------------------------------------------------------

class EmployeeForm(forms.ModelForm, EmployeeModelAndExcludeMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class EmployeeEditForm(forms.ModelForm, EmployeeModelAndExcludeMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class EmployeeDeleteForm(forms.ModelForm, EmployeeModelAndExcludeMixin):
    class Meta:
        model = Employee
        exclude = ['slug']

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

# ----------------------------------------------------------------------

class EmployeePositionForm(forms.Form):
    EMPLOYEE_POSITIONS_EN = (
        ('All', 'All'),
        ('Quality Manager', 'Quality Manager'),
        ('Quality Engineer', 'Quality Engineer'),
        ('Quality Inspector', 'Quality Inspector'),
    )

    EMPLOYEE_POSITIONS_BG = (
        ('All', 'Всички'),
        ('Quality Manager', 'Мениджър качество'),
        ('Quality Engineer', 'Инженер качество'),
        ('Quality Inspector', 'Инспектор качество'),
    )

    employee_position_dropdown = forms.ChoiceField(
        label='Select employee position',
        choices=EMPLOYEE_POSITIONS_EN,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if translation.get_language() == 'bg':
            self.fields['employee_position_dropdown'].label = 'Избери длъжност'
            self.fields['employee_position_dropdown'].choices = self.EMPLOYEE_POSITIONS_BG


# Trainings
# ----------------------------------------------------------------------

class TrainingsForm(forms.ModelForm, TrainingsModelAndExcludeMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class TrainingsEditForm(forms.ModelForm, TrainingsModelAndExcludeMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class TrainingsDeleteForm(forms.ModelForm, TrainingsModelAndExcludeMixin):
    class Meta:
        model = Trainings
        exclude = ['slug']

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
