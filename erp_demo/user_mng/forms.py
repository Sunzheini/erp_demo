from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class MySignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username')
        field_classes = {'username': UsernameField}


class MySignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
