from django.urls import path, include

from erp_demo.user_mng.views import SignUpView, SignInView, SignOutView, \
    UserDetailsView, EditUserView, DeleteUserView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='user details'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', DeleteUserView.as_view(), name='delete user'),
    ])),
]
