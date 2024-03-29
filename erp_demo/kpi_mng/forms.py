from django import forms
from django.utils import translation

from erp_demo.kpi_mng.models import Kpi


LABELS_EN = {
    'name': 'KPI name',
    'description': 'Description',
    'target': 'Target',
    'actual_01_23': 'Actual 01/23',
    'actual_02_23': 'Actual 02/23',
    'actual_03_23': 'Actual 03/23',
    'actual_04_23': 'Actual 04/23',
    'actual_05_23': 'Actual 05/23',
    'actual_06_23': 'Actual 06/23',
    'actual_07_23': 'Actual 07/23',
    'actual_08_23': 'Actual 08/23',
    'actual_09_23': 'Actual 09/23',
    'actual_10_23': 'Actual 10/23',
    'actual_11_23': 'Actual 11/23',
    'actual_12_23': 'Actual 12/23',
}

LABELS_BG = {
    'name': 'Име на KPI',
    'description': 'Описание',
    'target': 'Цел',
    'actual_01_23': 'Актуално 01/23',
    'actual_02_23': 'Актуално 02/23',
    'actual_03_23': 'Актуално 03/23',
    'actual_04_23': 'Актуално 04/23',
    'actual_05_23': 'Актуално 05/23',
    'actual_06_23': 'Актуално 06/23',
    'actual_07_23': 'Актуално 07/23',
    'actual_08_23': 'Актуално 08/23',
    'actual_09_23': 'Актуално 09/23',
    'actual_10_23': 'Актуално 10/23',
    'actual_11_23': 'Актуално 11/23',
    'actual_12_23': 'Актуално 12/23',
}

class KpiFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['description'].label = LABELS_BG['description']
            self.fields['target'].label = LABELS_BG['target']
            self.fields['actual_01_23'].label = LABELS_BG['actual_01_23']
            self.fields['actual_02_23'].label = LABELS_BG['actual_02_23']
            self.fields['actual_03_23'].label = LABELS_BG['actual_03_23']
            self.fields['actual_04_23'].label = LABELS_BG['actual_04_23']
            self.fields['actual_05_23'].label = LABELS_BG['actual_05_23']
            self.fields['actual_06_23'].label = LABELS_BG['actual_06_23']
            self.fields['actual_07_23'].label = LABELS_BG['actual_07_23']
            self.fields['actual_08_23'].label = LABELS_BG['actual_08_23']
            self.fields['actual_09_23'].label = LABELS_BG['actual_09_23']
            self.fields['actual_10_23'].label = LABELS_BG['actual_10_23']
            self.fields['actual_11_23'].label = LABELS_BG['actual_11_23']
            self.fields['actual_12_23'].label = LABELS_BG['actual_12_23']


class KpiForm(forms.ModelForm, KpiFormMixin):
    class Meta:
        model = Kpi
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class KpiEditForm(forms.ModelForm, KpiFormMixin):
    class Meta:
        model = Kpi
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class KpiDeleteForm(forms.ModelForm, KpiFormMixin):
    class Meta:
        model = Kpi
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


class KpiViewForm(forms.ModelForm, KpiFormMixin):
    class Meta:
        model = Kpi
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
