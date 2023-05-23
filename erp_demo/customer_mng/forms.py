from django import forms
from django.utils import translation

from erp_demo.customer_mng.models import Customer

LABELS_EN = {
            'type': 'Customer type',
            'attachment': 'Customer logo',
            'name': 'Customer name',
            'registration_address': 'Registration city address',
            'registration_city': 'Registration city',
            'eik': 'EIK',
            'mol1': 'MOL',
            'mol2': 'MOL 2',
            'mol3': 'MOL 3',
            'mol4': 'MOL 4',
            'mol5': 'MOL 5',
            'correspondence_address1': 'Correspondence address',
            'correspondence_address2': 'Correspondence address 2',
            'correspondence_address3': 'Correspondence address 3',
            'correspondence_address4': 'Correspondence address 4',
            'correspondence_address5': 'Correspondence address 5',
            'contact_person1': 'Contact person',
            'contact_person2': 'Contact person 2',
            'contact_person3': 'Contact person 3',
            'contact_person4': 'Contact person 4',
            'contact_person5': 'Contact person 5',
            'phone1': 'Phone',
            'phone2': 'Phone 2',
            'phone3': 'Phone 3',
            'phone4': 'Phone 4',
            'phone5': 'Phone 5',
            'email1': 'Email',
            'email2': 'Email 2',
            'email3': 'Email 3',
            'email4': 'Email 4',
            'email5': 'Email 5',
        }

LABELS_BG = {
            'type': 'Тип на клиента',
            'attachment': 'Лого на клиента',
            'name': 'Име на клиента',
            'registration_address': 'Адрес по регистрация',
            'registration_city': 'Населено място',
            'eik': 'ЕИК',
            'mol1': 'МОЛ',
            'mol2': 'МОЛ 2',
            'mol3': 'МОЛ 3',
            'mol4': 'МОЛ 4',
            'mol5': 'МОЛ 5',
            'correspondence_address1': 'Адрес за кореспонденция',
            'correspondence_address2': 'Адрес за кореспонденция 2',
            'correspondence_address3': 'Адрес за кореспонденция 3',
            'correspondence_address4': 'Адрес за кореспонденция 4',
            'correspondence_address5': 'Адрес за кореспонденция 5',
            'contact_person1': 'Лице за контакт',
            'contact_person2': 'Лице за контакт 2',
            'contact_person3': 'Лице за контакт 3',
            'contact_person4': 'Лице за контакт 4',
            'contact_person5': 'Лице за контакт 5',
            'phone1': 'Телефон',
            'phone2': 'Телефон 2',
            'phone3': 'Телефон 3',
            'phone4': 'Телефон 4',
            'phone5': 'Телефон 5',
            'email1': 'Имейл',
            'email2': 'Имейл 2',
            'email3': 'Имейл 3',
            'email4': 'Имейл 4',
            'email5': 'Имейл 5',
        }

CHOICES_BG=(
    ('', 'Празно'),
    ('Физическо лице', 'Физическо лице'),
    ('Юридическо лице', 'Юридическо лице'),
    ('Институция', 'Институция'),
)

class CustFormMixin:
    def change_labels_to_bg(self):
        language_code = translation.get_language()
        if language_code == 'bg':
            try:
                self.fields['type'].label = LABELS_BG['type']
                self.fields['type'].choices = CHOICES_BG
            except KeyError:
                pass

            try:
                self.fields['attachment'].label = LABELS_BG['attachment']
            except KeyError:
                pass

            self.fields['name'].label = LABELS_BG['name']
            self.fields['registration_address'].label = LABELS_BG['registration_address']
            self.fields['registration_city'].label = LABELS_BG['registration_city']
            self.fields['eik'].label = LABELS_BG['eik']
            self.fields['mol1'].label = LABELS_BG['mol1']
            self.fields['mol2'].label = LABELS_BG['mol2']
            self.fields['mol3'].label = LABELS_BG['mol3']
            self.fields['mol4'].label = LABELS_BG['mol4']
            self.fields['mol5'].label = LABELS_BG['mol5']
            self.fields['correspondence_address1'].label = LABELS_BG['correspondence_address1']
            self.fields['correspondence_address2'].label = LABELS_BG['correspondence_address2']
            self.fields['correspondence_address3'].label = LABELS_BG['correspondence_address3']
            self.fields['correspondence_address4'].label = LABELS_BG['correspondence_address4']
            self.fields['correspondence_address5'].label = LABELS_BG['correspondence_address5']
            self.fields['contact_person1'].label = LABELS_BG['contact_person1']
            self.fields['contact_person2'].label = LABELS_BG['contact_person2']
            self.fields['contact_person3'].label = LABELS_BG['contact_person3']
            self.fields['contact_person4'].label = LABELS_BG['contact_person4']
            self.fields['contact_person5'].label = LABELS_BG['contact_person5']
            self.fields['phone1'].label = LABELS_BG['phone1']
            self.fields['phone2'].label = LABELS_BG['phone2']
            self.fields['phone3'].label = LABELS_BG['phone3']
            self.fields['phone4'].label = LABELS_BG['phone4']
            self.fields['phone5'].label = LABELS_BG['phone5']
            self.fields['email1'].label = LABELS_BG['email1']
            self.fields['email2'].label = LABELS_BG['email2']
            self.fields['email3'].label = LABELS_BG['email3']
            self.fields['email4'].label = LABELS_BG['email4']
            self.fields['email5'].label = LABELS_BG['email5']


class CustomerForm(forms.ModelForm, CustFormMixin):
    class Meta:
        model = Customer
        exclude = ['slug']

        labels = LABELS_EN

        widgets = {
            'type': forms.RadioSelect(
            ),
            'attachment': forms.ClearableFileInput(
                attrs={
                    'class': 'file-input',
                    'accept': 'image/*',
                }
            ),
            # 'name': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Пълно име (с правната форма)',
            #     }
            # ),
            # 'registration_address': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Адрес по търговски регистър',
            #     }
            # ),
            # 'registration_city': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Населено място по търговски регистър',
            #     }
            # ),
            # 'eik': forms.NumberInput(
            #     attrs={
            #         'placeholder': 'ЕИК',
            #     }
            # ),
            # 'mol1': forms.TextInput(
            #     attrs={
            #         'placeholder': 'МОЛ',
            #     }
            # ),
            # 'correspondence_address1': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Основен адрес за кореспонденция',
            #     }
            # ),
            # 'contact_person1': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Основно лице за контакт',
            #     }
            # ),
            # 'phone1': forms.TextInput(
            #     attrs={
            #         'placeholder': '+359 xx xxx xxx',
            #     }
            # ),
            # 'email1': forms.EmailInput(
            #     attrs={
            #         'placeholder': 'Валиден имейл адрес',
            #     }
            # ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class CustomerEditForm(forms.ModelForm, CustFormMixin):
    class Meta:
        model = Customer
        exclude = ['slug']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()


class CustomerDeleteForm(forms.ModelForm, CustFormMixin):
    class Meta:
        model = Customer
        exclude = ['slug', 'type', 'attachment']

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


class CustomerViewForm(forms.ModelForm, CustFormMixin):
    class Meta:
        model = Customer
        exclude = ['slug', 'attachment']

        labels = LABELS_EN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_labels_to_bg()
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
