from django import forms

from erp_demo.customer_mng.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug']

        labels = {
            'type': 'Тип на клиента',
            'name': 'Име на клиента',
            'registration_address': 'Адрес по регистрация',
            'registration_city': 'Населено място',
            'eik': 'ЕИК',
            'mol': 'МОЛ',
            'correspondence_address': 'Адрес за кореспонденция',
            'contact_person': 'Лице за контакт',
            'phone': 'Телефон',
            'email': 'Имейл',
        }

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

        labels = {
            'type': 'Тип на клиента',
            'name': 'Име на клиента',
            'registration_address': 'Адрес по регистрация',
            'registration_city': 'Населено място',
            'eik': 'ЕИК',
            'mol': 'МОЛ',
            'correspondence_address': 'Адрес за кореспонденция',
            'contact_person': 'Лице за контакт',
            'phone': 'Телефон',
            'email': 'Имейл',
        }


class CustomerDeleteForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug', 'type']

        labels = {
            'type': 'Тип на клиента',
            'name': 'Име на клиента',
            'registration_address': 'Адрес по регистрация',
            'registration_city': 'Населено място',
            'eik': 'ЕИК',
            'mol': 'МОЛ',
            'correspondence_address': 'Адрес за кореспонденция',
            'contact_person': 'Лице за контакт',
            'phone': 'Телефон',
            'email': 'Имейл',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance