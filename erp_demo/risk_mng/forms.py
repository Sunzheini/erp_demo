from django import forms
from django.utils import translation

from erp_demo.risk_mng.models import Risk


LABELS_EN = {
    'name': 'Risk name',
    'description': 'Description',
    'probability': 'Probability',
    'impact': 'Impact',
    'immediate_action': 'Immediate action',
    'ia_test_period': 'IA test period',
    'long_term_action': 'Long term action',
    'new_probability': 'New probability',
    'new_impact': 'New impact',
}

LABELS_BG = {
    'name': 'Име на риск',
    'description': 'Описание',
    'probability': 'Вероятност',
    'impact': 'Въздействие',
    'immediate_action': 'Незабавно действие',
    'ia_test_period': 'Период на тест на НД',
    'long_term_action': 'Дългосрочно действие',
    'new_probability': 'Нова вероятност',
    'new_impact': 'Ново въздействие',
}


class RiskFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['description'].label = LABELS_BG['description']
            self.fields['probability'].label = LABELS_BG['probability']
            self.fields['impact'].label = LABELS_BG['impact']
            self.fields['immediate_action'].label = LABELS_BG['immediate_action']
            self.fields['ia_test_period'].label = LABELS_BG['ia_test_period']
            self.fields['long_term_action'].label = LABELS_BG['long_term_action']
            self.fields['new_probability'].label = LABELS_BG['new_probability']
            self.fields['new_impact'].label = LABELS_BG['new_impact']


class RiskForm(forms.ModelForm, RiskFormMixin):
    class Meta:
        model = Risk
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class RiskEditForm(forms.ModelForm, RiskFormMixin):
    class Meta:
        model = Risk
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class RiskDeleteForm(forms.ModelForm, RiskFormMixin):
    class Meta:
        model = Risk
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


class RiskViewForm(forms.ModelForm, RiskFormMixin):
    class Meta:
        model = Risk
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
