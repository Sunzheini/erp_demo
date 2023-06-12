from django import forms
from django.utils import translation

from erp_demo.newactions_mng.models import NewAction


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

STATUS_CHOICES_BG = (
    ('Not Started', 'Не започнато'),
    ('Ongoing', 'Изпълнява се'),
    ('Completed', 'Завършено'),
)


class NewActionFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            for field in self.fields:
                self.fields[field].label = LABELS_BG[field]
            self.fields['status'].choices = STATUS_CHOICES_BG


class NewActionForm(NewActionFormMixin, forms.ModelForm):
    class Meta:
        model = NewAction
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


class NewActionEditForm(NewActionFormMixin, forms.ModelForm):
    class Meta:
        model = NewAction
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


class NewActionDeleteForm(NewActionFormMixin, forms.ModelForm):
    class Meta:
        model = NewAction
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


class NewActionViewForm(NewActionFormMixin, forms.ModelForm):
    class Meta:
        model = NewAction
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
