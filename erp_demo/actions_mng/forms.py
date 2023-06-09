from django import forms
from django.utils import translation

from django.contrib.contenttypes.models import ContentType
from erp_demo.actions_mng.models import Action


LABELS_EN = {
    'type': 'Type',
    'scope': 'Scope',
    'content_type': 'Content type',
    'object_id': 'Object id',
    'name': 'Name',
    'responsible': 'Responsible',
    'target_date': 'Target date',
    'comments': 'Comments',
    'status': 'Status',
}

LABELS_BG = {
    'type': 'Тип',
    'scope': 'Обхват',
    'content_type': 'Тип съдържание',
    'object_id': 'ID на обект',
    'name': 'Име',
    'responsible': 'Отговорник',
    'target_date': 'Целева дата',
    'comments': 'Коментари',
    'status': 'Статус',
}


class ActionFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            for field in self.fields:
                try:
                    self.fields[field].label = LABELS_BG[field]
                except KeyError:
                    pass


class ActionForm(ActionFormMixin, forms.ModelForm):
    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model__in=['nonconformity', 'opportunity', 'risk']),
        label='Content type'
    )
    object_id = forms.ChoiceField(choices=[], label='Object id')

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionEditForm(ActionFormMixin, forms.ModelForm):
    content_type = forms.ModelChoiceField(
        queryset=ContentType.objects.filter(model__in=['nonconformity', 'opportunity', 'risk']),
        label='Content type'
    )
    object_id = forms.ChoiceField(choices=[], label='Object id')

    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'target_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class ActionDeleteForm(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
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


class ActionViewForm(ActionFormMixin, forms.ModelForm):
    class Meta:
        model = Action
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
