from django import forms
from django.utils import translation

from erp_demo.nonconformity_mng.models import Nonconformity


LABELS_EN = {
    'customer': 'Customer',
    'customer_claim_number': 'Customer claim number',
    'customer_claim_date': 'Customer claim date',
    'internal_claim_number': 'Internal claim number',
    'nonconformity_start_date': 'Nonconformity start date',
    'part_number': 'Part number',
    'part_revision': 'Part revision',
    'part_name': 'Part name',

    'name': 'Customer definition',
    'internal_definition': 'Internal definition',

    'nonconformity_owner': 'Nonconformity owner',
    'team_members': 'Team members',

    'containment_actions': 'Containment actions',
    'correction_actions': 'Correction actions',

    'possible_root_cause1': 'Possible root cause 1',
    'cause1_ask_why1': 'Cause 1 Ask Why 1',
    'cause1_ask_why2': 'Cause 1 Ask Why 2',
    'cause1_ask_why3': 'Cause 1 Ask Why 3',
    'cause1_ask_why4': 'Cause 1 Ask Why 4',
    'cause1_ask_why5': 'Cause 1 Ask Why 5',

    'possible_root_cause2': 'Possible root cause 2',
    'cause2_ask_why1': 'Cause 2 Ask Why 1',
    'cause2_ask_why2': 'Cause 2 Ask Why 2',
    'cause2_ask_why3': 'Cause 2 Ask Why 3',
    'cause2_ask_why4': 'Cause 2 Ask Why 4',
    'cause2_ask_why5': 'Cause 2 Ask Why 5',

    'possible_root_cause3': 'Possible root cause 3',
    'cause3_ask_why1': 'Cause 3 Ask Why 1',
    'cause3_ask_why2': 'Cause 3 Ask Why 2',
    'cause3_ask_why3': 'Cause 3 Ask Why 3',
    'cause3_ask_why4': 'Cause 3 Ask Why 4',
    'cause3_ask_why5': 'Cause 3 Ask Why 5',

    'possible_root_cause4': 'Possible root cause 4',
    'cause4_ask_why1': 'Cause 4 Ask Why 1',
    'cause4_ask_why2': 'Cause 4 Ask Why 2',
    'cause4_ask_why3': 'Cause 4 Ask Why 3',
    'cause4_ask_why4': 'Cause 4 Ask Why 4',
    'cause4_ask_why5': 'Cause 4 Ask Why 5',

    'possible_root_cause5': 'Possible root cause 5',
    'cause5_ask_why1': 'Cause 5 Ask Why 1',
    'cause5_ask_why2': 'Cause 5 Ask Why 2',
    'cause5_ask_why3': 'Cause 5 Ask Why 3',
    'cause5_ask_why4': 'Cause 5 Ask Why 4',
    'cause5_ask_why5': 'Cause 5 Ask Why 5',

    'permanent_corrective_actions': 'Permanent corrective actions',
    'breakpoint_batch_number': 'Breakpoint batch number',
    'breakpoint_at_customer_date': 'Breakpoint at customer date',

    'systematic_actions': 'Systematic actions',
}

LABELS_BG = {
    'customer': 'Клиент',
    'customer_claim_number': 'Номер рекламация клиент',
    'customer_claim_date': 'Дата рекламацията клиент',
    'internal_claim_number': 'Вътрешен номер',
    'nonconformity_start_date': 'Дата стартиране',
    'part_number': 'Номер на изделието',
    'part_revision': 'Ревизия на изделието',
    'part_name': 'Име на изделието',

    'name': 'Дефиниция на клиента',
    'internal_definition': 'Вътрешна дефиниция',

    'nonconformity_owner': 'Отговорник за рекламацията',
    'team_members': 'Членове на екипа',

    'containment_actions': 'Действия за задържане',
    'correction_actions': 'Действия за корекция',

    'possible_root_cause1': 'Възможна коренна причина 1',
    'cause1_ask_why1': 'Причина 1 Попитай Защо 1',
    'cause1_ask_why2': 'Причина 1 Попитай Защо 2',
    'cause1_ask_why3': 'Причина 1 Попитай Защо 3',
    'cause1_ask_why4': 'Причина 1 Попитай Защо 4',
    'cause1_ask_why5': 'Причина 1 Попитай Защо 5',

    'possible_root_cause2': 'Възможна коренна причина 2',
    'cause2_ask_why1': 'Причина 2 Попитай Защо 1',
    'cause2_ask_why2': 'Причина 2 Попитай Защо 2',
    'cause2_ask_why3': 'Причина 2 Попитай Защо 3',
    'cause2_ask_why4': 'Причина 2 Попитай Защо 4',
    'cause2_ask_why5': 'Причина 2 Попитай Защо 5',

    'possible_root_cause3': 'Възможна коренна причина 3',
    'cause3_ask_why1': 'Причина 3 Попитай Защо 1',
    'cause3_ask_why2': 'Причина 3 Попитай Защо 2',
    'cause3_ask_why3': 'Причина 3 Попитай Защо 3',
    'cause3_ask_why4': 'Причина 3 Попитай Защо 4',
    'cause3_ask_why5': 'Причина 3 Попитай Защо 5',

    'possible_root_cause4': 'Възможна коренна причина 4',
    'cause4_ask_why1': 'Причина 4 Попитай Защо 1',
    'cause4_ask_why2': 'Причина 4 Попитай Защо 2',
    'cause4_ask_why3': 'Причина 4 Попитай Защо 3',
    'cause4_ask_why4': 'Причина 4 Попитай Защо 4',
    'cause4_ask_why5': 'Причина 4 Попитай Защо 5',

    'possible_root_cause5': 'Възможна коренна причина 5',
    'cause5_ask_why1': 'Причина 5 Попитай Защо 1',
    'cause5_ask_why2': 'Причина 5 Попитай Защо 2',
    'cause5_ask_why3': 'Причина 5 Попитай Защо 3',
    'cause5_ask_why4': 'Причина 5 Попитай Защо 4',
    'cause5_ask_why5': 'Причина 5 Попитай Защо 5',

    'permanent_corrective_actions': 'Постоянни коригиращи действия',
    'breakpoint_batch_number': 'Номер на първа ОК партида',
    'breakpoint_at_customer_date': 'Дата на първа ОК партида при клиента',

    'systematic_actions': 'Систематични действия',
}


class NonconformityFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            for field in self.fields:
                self.fields[field].label = LABELS_BG[field]


class NonconformityForm(NonconformityFormMixin, forms.ModelForm):
    class Meta:
        model = Nonconformity
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'customer_claim_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',  # taka veshe izkarva kalendara
                }
            ),
            'nonconformity_start_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'breakpoint_at_customer_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class NonconformityEditForm(NonconformityFormMixin, forms.ModelForm):
    class Meta:
        model = Nonconformity
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'customer_claim_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',  # taka veshe izkarva kalendara
                }
            ),
            'nonconformity_start_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
            'breakpoint_at_customer_date': forms.DateInput(
                attrs={
                    'placeholder': 'dd-mmm-yyyy',
                    'type': 'date',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class NonconformityDeleteForm(NonconformityFormMixin, forms.ModelForm):
    class Meta:
        model = Nonconformity
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


class NonconformityViewForm(NonconformityFormMixin, forms.ModelForm):
    class Meta:
        model = Nonconformity
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
