from django.contrib.auth.views import LoginView
from django.urls import path, include

from erp_demo.user_mng.views import SignUpView, my_login, SignInView, SignOutView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    # path('login/', my_login, name='login'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
]
