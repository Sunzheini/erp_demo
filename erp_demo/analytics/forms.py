from django import forms
from django.utils import translation
from erp_demo.analytics.models import Analysis


ANALYSIS_LABELS_EN = {
    'name': 'Name',
    'code': 'Code',
    'measurement_unit': 'Measurement unit',
    'materials': 'Materials',
    'work_force': 'Work force',
    'machines': 'Machines',
}

ANALYSIS_LABELS_BG = {
    'name': 'Име',
    'code': 'Код',
    'measurement_unit': 'Мерна единица',
    'materials': 'Материали',
    'work_force': 'Работна сила',
    'machines': 'Машини',
}


class AnalysisModelAndExcludeMixin:
    model = Analysis
    exclude = ['slug']

    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = ANALYSIS_LABELS_BG['name']
            self.fields['code'].label = ANALYSIS_LABELS_BG['code']
            self.fields['measurement_unit'].label = ANALYSIS_LABELS_BG['measurement_unit']
            self.fields['materials'].label = ANALYSIS_LABELS_BG['materials']
            self.fields['work_force'].label = ANALYSIS_LABELS_BG['work_force']
            self.fields['machines'].label = ANALYSIS_LABELS_BG['machines']
        else:
            self.fields['name'].label = ANALYSIS_LABELS_EN['name']
            self.fields['code'].label = ANALYSIS_LABELS_EN['code']
            self.fields['measurement_unit'].label = ANALYSIS_LABELS_EN['measurement_unit']
            self.fields['materials'].label = ANALYSIS_LABELS_EN['materials']
            self.fields['work_force'].label = ANALYSIS_LABELS_EN['work_force']
            self.fields['machines'].label = ANALYSIS_LABELS_EN['machines']


class AnalysisForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class AnalysisEditForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class AnalysisDeleteForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

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


class AnalysisViewForm(forms.ModelForm, AnalysisModelAndExcludeMixin):
    class Meta:
        model = Analysis
        exclude = ['slug']

        labels = ANALYSIS_LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
