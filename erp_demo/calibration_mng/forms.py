from django import forms
from django.utils import translation

from erp_demo.calibration_mng.models import MeasuringEquipment


LABELS_EN = {
    'name': 'Equipment Name',
    'inventory_number': 'Inventory Number',
    'characteristics': 'Characteristics',
    'installation_date': 'Installation Date',
    'calibration_interval_in_days': 'Calibration Interval In Days',
}

LABELS_BG = {
    'name': 'Наименование',
    'inventory_number': 'Инвентарен номер',
    'characteristics': 'Характеристики',
    'installation_date': 'Дата инсталиране',
    'calibration_interval_in_days': 'Интервал на калибровка в дни',
}


class MeasuringEquipmentFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['inventory_number'].label = LABELS_BG['inventory_number']
            self.fields['characteristics'].label = LABELS_BG['characteristics']
            self.fields['installation_date'].label = LABELS_BG['installation_date']
            self.fields['calibration_interval_in_days'].label = LABELS_BG['calibration_interval_in_days']


class MeasuringEquipmentForm(forms.ModelForm, MeasuringEquipmentFormMixin):
    class Meta:
        model = MeasuringEquipment
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


class MeasuringEquipmentEditForm(forms.ModelForm, MeasuringEquipmentFormMixin):
    class Meta:
        model = MeasuringEquipment
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


class MeasuringEquipmentDeleteForm(forms.ModelForm, MeasuringEquipmentFormMixin):
    class Meta:
        model = MeasuringEquipment
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


class MeasuringEquipmentShowForm(forms.ModelForm, MeasuringEquipmentFormMixin):
    class Meta:
        model = MeasuringEquipment
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
