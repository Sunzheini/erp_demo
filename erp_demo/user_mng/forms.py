from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

# from erp_demo.user_mng.models import Profile


UserModel = get_user_model()


class UserMngCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        # fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}


class UserEditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'username': UsernameField}


# class MySignUpForm(UserMngCreationForm):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField()
#
#     class Meta:
#         model = UserModel
#         fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age')
#
#     def save(self, commit=True):
#         user = super().save(commit=commit)
#         profile = Profile(
#             user=user,
#             first_name=self.cleaned_data['first_name'],
#             last_name=self.cleaned_data['last_name'],
#             age=self.cleaned_data['age'],
#         )
#         if commit:
#             profile.save()
#         return user
#
#
# class MySignInForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
