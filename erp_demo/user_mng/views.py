from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from erp_demo.user_mng.forms import UserMngCreationForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'user_mng/sign_up.html'
    form_class = UserMngCreationForm
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    template_name = 'user_mng/login.html'
    success_url = reverse_lazy('index')
    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(LogoutView):
    template_name = 'user_mng/logout.html'
    # next_page = reverse_lazy('index')     # here or in settings.py


class UserDetailsView(views.DetailView):
    template_name = 'user_mng/user_details.html'
    model = UserModel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if the owner of the profile sees it, he can edit / delete it
        context['is_owner'] = self.request.user == self.object
        return context


class EditUserView(views.UpdateView):
    template_name = 'user_mng/edit_user.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email')
    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk': self.request.user.pk})


class DeleteUserView(views.DeleteView):
    template_name = 'user_mng/delete_user.html'
    model = UserModel
    success_url = reverse_lazy('index')
