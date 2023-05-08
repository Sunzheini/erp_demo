from django.urls import path, include

# from erp_demo.customer_mng.views import CustomerAppViews

from erp_demo.main_app.custom_prototypes import PrototypeViews
from erp_demo.customer_mng.forms import CustomerForm, CustomerEditForm, CustomerDeleteForm, CustomerViewForm
from erp_demo.customer_mng.models import Customer

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'customer_mng/customer_mng_index.html',
    'customer_mng/customer_list.html',
    'customer_mng/add_customer.html',
    'customer_mng/show_customer.html',
    'customer_mng/edit_customer.html',
    'customer_mng/delete_customer.html',
]

redirect_url = 'customer list'

form_list = [
    CustomerForm, CustomerViewForm, CustomerEditForm, CustomerDeleteForm,
]

files_are_used = True

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', PrototypeViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).index_view, name='customer mng index'),

    path('customer-list/', PrototypeViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).list_view, name='customer list'),

    path('add-customer/', PrototypeViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).create_view, name='add customer'),

    path('show-customer/<int:pk>/<slug:slug>/', PrototypeViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).show_view, name='show customer'),

    path('edit-customer/<int:pk>/<slug:slug>/', PrototypeViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).edit_view, name='edit customer'),

    path('delete-customer/<int:pk>/<slug:slug>/', PrototypeViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).delete_view, name='delete customer'),
]

# urlpatterns = [
#     path('', CustomerAppViews().customer_mng_index, name='customer mng index'),
#     path('customer-list/', CustomerAppViews().customer_list, name='customer list'),
#     path('add-customer/', CustomerAppViews().add_customer, name='add customer'),
#     path('show-customer/<int:pk>/<slug:slug>/', CustomerAppViews().show_customer, name='show customer'),
#     path('edit-customer/<int:pk>/<slug:slug>/', CustomerAppViews().edit_customer, name='edit customer'),
#     path('delete-customer/<int:pk>/<slug:slug>/', CustomerAppViews().delete_customer, name='delete customer'),
# ]