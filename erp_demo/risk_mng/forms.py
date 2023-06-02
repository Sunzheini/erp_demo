from django import forms
from django.utils import translation

from erp_demo.risk_mng.models import Risk


LABELS_EN = {
    'name': 'Risk name',
}

LABELS_BG = {
    'name': 'Име на риск',
}


class RiskFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']


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
