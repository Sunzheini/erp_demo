from django import forms
from django.utils import translation

from erp_demo.maintenance_mng.models import Machine


LABELS_EN = {
    'name': 'Machine Name',
    'inventory_number': 'Inventory Number',
    'characteristics': 'Characteristics',
    'installation_date': 'Installation Date',
    'maintenance_interval_in_days': 'Maintenance Interval In Days',
}

LABELS_BG = {
    'name': 'Наименование',
    'inventory_number': 'Инвентарен номер',
    'characteristics': 'Характеристики',
    'installation_date': 'Дата инсталиране',
    'maintenance_interval_in_days': 'Интервал на поддръжка в дни',
}


class MachineFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['inventory_number'].label = LABELS_BG['inventory_number']
            self.fields['characteristics'].label = LABELS_BG['characteristics']
            self.fields['installation_date'].label = LABELS_BG['installation_date']
            self.fields['maintenance_interval_in_days'].label = LABELS_BG['maintenance_interval_in_days']


class MachineForm(forms.ModelForm, MachineFormMixin):
    class Meta:
        model = Machine
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'installation_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class MachineEditForm(forms.ModelForm, MachineFormMixin):
    class Meta:
        model = Machine
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'installation_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class MachineDeleteForm(forms.ModelForm, MachineFormMixin):
    class Meta:
        model = Machine
        exclude = ['slug']

        labels = LABELS_EN

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


class MachineViewForm(forms.ModelForm, MachineFormMixin):
    class Meta:
        model = Machine
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
