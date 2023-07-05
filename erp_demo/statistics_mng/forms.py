from django import forms
from django.utils import translation

from erp_demo.statistics_mng.models import StatModel1


LABELS_EN = {
    'name': 'Record Number',
    'operator': 'Operator ID',
    'grinding': 'Grinding defects',
    'welding': 'Welding defects',
    'blasting': 'Blasting defects',
    'painting': 'Painting defects',
    'assembly': 'Assembly defects',
    'total_pieces': 'Total pieces produced',
}

LABELS_BG = {
    'name': 'Номер Запис',
    'operator': 'ID оператор',
    'grinding': 'Дефекти шлайфане',
    'welding': 'Дефекти заваряване',
    'blasting': 'Дефекти пясъкоструене',
    'painting': 'Дефекти боядисване',
    'assembly': 'Дефекти монтаж',
    'total_pieces': 'Общо произведени бр.',
}


# for uploading excels
# --------------------------------------------------------------------
class StatModel1UploadForm(forms.Form):

    select_file = forms.FileField(
        label='',
    )


# --------------------------------------------------------------------

class StatModel1FormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            for field in self.fields:
                self.fields[field].label = LABELS_BG[field]


class StatModel1Form(StatModel1FormMixin, forms.ModelForm):
    class Meta:
        model = StatModel1
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class StatModel1EditForm(StatModel1FormMixin, forms.ModelForm):
    class Meta:
        model = StatModel1
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class StatModel1DeleteForm(StatModel1FormMixin, forms.ModelForm):
    class Meta:
        model = StatModel1
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


class StatModel1ViewForm(StatModel1FormMixin, forms.ModelForm):
    class Meta:
        model = StatModel1
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
