from django import forms
from django.utils import translation

from erp_demo.interaction_mng.models import Interaction


LABELS_EN = {
    'name': 'Interaction name',
    'from_process_step': 'From process step',
    'to_process_step': 'To process step',
    'documents': 'Documents',
}

LABELS_BG = {
    'name': 'Взаимодействие',
    'from_process_step': 'От процесна стъпка',
    'to_process_step': 'Към процесна стъпка',
    'documents': 'Документи',
}


class InteractionFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['name'].label = LABELS_BG['name']
            self.fields['from_process_step'].label = LABELS_BG['from_process_step']
            self.fields['to_process_step'].label = LABELS_BG['to_process_step']
            self.fields['documents'].label = LABELS_BG['documents']


class InteractionForm(forms.ModelForm, InteractionFormMixin):
    class Meta:
        model = Interaction
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class InteractionEditForm(forms.ModelForm, InteractionFormMixin):
    class Meta:
        model = Interaction
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class InteractionDeleteForm(forms.ModelForm, InteractionFormMixin):
    class Meta:
        model = Interaction
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


class InteractionViewForm(forms.ModelForm, InteractionFormMixin):
    class Meta:
        model = Interaction
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
