from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

UserModel = get_user_model()


class UserMngCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': UsernameField}
