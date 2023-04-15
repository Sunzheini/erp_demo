from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views

from erp_demo.user_mng.forms import MySignUpForm, MySignInForm


class SignUpView(views.CreateView):
    template_name = 'user_mng/sign_up.html'
    form_class = MySignUpForm
    success_url = reverse_lazy('index')

    # signs user in
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


# not used
def my_login(request):
    if request.method == 'GET':
        form = MySignInForm()
    else:
        form = MySignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
    context = {
        'form': form,
    }
    return render(request, 'user_mng/login.html', context)


class SignInView(LoginView):
    template_name = 'user_mng/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(LogoutView):
    template_name = 'user_mng/logout.html'
