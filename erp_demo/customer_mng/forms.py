from django import forms

from erp_demo.customer_mng.models import Customer

LABELS = {
            'type': 'Тип на клиента',
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

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug']

        labels = LABELS

        widgets = {
            'type': forms.RadioSelect(
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Пълно име (с правната форма)',
                }
            ),
            'registration_address': forms.TextInput(
                attrs={
                    'placeholder': 'Адрес по търговски регистър',
                }
            ),
            'registration_city': forms.TextInput(
                attrs={
                    'placeholder': 'Населено място по търговски регистър',
                }
            ),
            'eik': forms.NumberInput(
                attrs={
                    'placeholder': 'ЕИК',
                }
            ),
            'mol': forms.TextInput(
                attrs={
                    'placeholder': 'МОЛ',
                }
            ),
            'correspondence_address': forms.TextInput(
                attrs={
                    'placeholder': 'Основен адрес за кореспонденция',
                }
            ),
            'contact_person': forms.TextInput(
                attrs={
                    'placeholder': 'Основно лице за контакт',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': '+359 xx xxx xxx',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Валиден имейл адрес',
                }
            ),
        }


class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug']

        labels = LABELS


class CustomerDeleteForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug', 'type']

        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance


class CustomerViewForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug']

        labels = LABELS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
