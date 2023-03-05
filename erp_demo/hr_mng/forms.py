import os
from django import forms
from erp_demo.hr_mng.models import Employee, Trainings


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


class TrainingsModelAndExcludeMixin:
    class Meta:
        model = Trainings
        exclude = ['slug']


# ----------------------------------------------------------------------

class EmployeeForm(forms.ModelForm, EmployeeModelAndExcludeMixin):
    pass


class EmployeeEditForm(forms.ModelForm, EmployeeModelAndExcludeMixin):
    pass


class EmployeeDeleteForm(forms.ModelForm, EmployeeModelAndExcludeMixin):
    class Meta:
        model = Employee
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


# ----------------------------------------------------------------------

class EmployeePositionForm(forms.Form):
    EMPLOYEE_POSITIONS = (
        ('All', 'All'),
        ('Quality Manager', 'Quality Manager'),
        ('Quality Engineer', 'Quality Engineer'),
        ('Quality Inspector', 'Quality Inspector'),
    )

    employee_position_dropdown = forms.ChoiceField(
        label='Select employee position',
        choices=EMPLOYEE_POSITIONS,
    )


# Trainings
# ----------------------------------------------------------------------

class TrainingsForm(forms.ModelForm, TrainingsModelAndExcludeMixin):
    pass


class TrainingsEditForm(forms.ModelForm, TrainingsModelAndExcludeMixin):
    pass


class TrainingsDeleteForm(forms.ModelForm, TrainingsModelAndExcludeMixin):
    class Meta:
        model = Trainings
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
