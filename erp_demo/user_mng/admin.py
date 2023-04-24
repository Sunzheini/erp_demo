from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

# from erp_demo.user_mng.forms import MySignUpForm

UserModel = get_user_model()


# @admin.register(UserModel)
# class AppUserAdmin(UserAdmin):
#     ordering = ('email',)
#     list_display = ['email', 'date_joined', 'last_login']
#     list_filter = ()
#     add_form = MySignUpForm
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#             },
#         ),
#         (None, {
#             'classes': ('wide',),
#             'fields': ('first_name', 'last_name', 'age'),
#             },
#         ),
#     )
#     readonly_fields = ['date_joined']


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    pass