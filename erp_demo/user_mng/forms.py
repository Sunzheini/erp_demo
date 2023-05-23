from django import forms
from django.utils import translation
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

UserModel = get_user_model()


CREATION_LABELS_EN = {
    'username': 'Username',
    'email': 'Email',
    'password1': 'Password',
    'password2': 'Password confirmation',
}

CREATION_LABELS_BG = {
    'username': 'Потребителско име',
    'email': 'Имейл',
    'password1': 'Парола',
    'password2': 'Потвърждение на паролата',
}

CHANGE_LABELS_EN = {
    'first_name': 'First name',
    'last_name': 'Last name',
    'email': 'Email',
}

CHANGE_LABELS_BG = {
    'first_name': 'Име',
    'last_name': 'Фамилия',
    'email': 'Имейл',
}


class UserMngCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['username'].label = CREATION_LABELS_BG['username']
            self.fields['email'].label = CREATION_LABELS_BG['email']
            self.fields['password1'].label = CREATION_LABELS_BG['password1']
            self.fields['password2'].label = CREATION_LABELS_BG['password2']


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        language_code = translation.get_language()
        if language_code == 'bg':
            self.fields['first_name'].label = CHANGE_LABELS_BG['first_name']
            self.fields['last_name'].label = CHANGE_LABELS_BG['last_name']
            self.fields['email'].label = CHANGE_LABELS_BG['email']
