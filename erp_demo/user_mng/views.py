from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from erp_demo.user_mng.models import AppUser
from erp_demo.user_mng.forms import UserMngCreationForm
#
# from erp_demo.user_mng.forms import MySignUpForm, MySignInForm


UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'user_mng/sign_up.html'
    # model = UserModel
    # fields = ('username', 'password')
    # form_class = MySignUpForm
    form_class = UserMngCreationForm
    success_url = reverse_lazy('index')

    # signs user in
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     login(self.request, self.object)
    #     return result


# # not used
# def my_login(request):
#     if request.method == 'GET':
#         form = MySignInForm()
#     else:
#         form = MySignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'user_mng/login.html', context)


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
