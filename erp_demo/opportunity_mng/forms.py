from django import forms
from django.utils import translation

from erp_demo.opportunity_mng.models import Opportunity


LABELS_EN = {
    'name': 'Opportunity for improvement name',
}

LABELS_BG = {
    'name': 'Име на възможност за подобрение',
}

class OpportunityFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']


class OpportunityForm(forms.ModelForm, OpportunityFormMixin):
    class Meta:
        model = Opportunity
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class OpportunityEditForm(forms.ModelForm, OpportunityFormMixin):
    class Meta:
        model = Opportunity
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class OpportunityDeleteForm(forms.ModelForm, OpportunityFormMixin):
    class Meta:
        model = Opportunity
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


class OpportunityViewForm(forms.ModelForm, OpportunityFormMixin):
    class Meta:
        model = Opportunity
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
