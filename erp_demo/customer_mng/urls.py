from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from erp_demo.customer_mng.views import CustomerAppViews

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
    # Create, View, Edit, Delete
    CustomerForm, CustomerViewForm, CustomerEditForm, CustomerDeleteForm,
]

files_are_used = True

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', CustomerAppViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).index_view, name='customer mng index'),

    path('customer-list/', CustomerAppViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).list_view, name='customer list'),

    path('add-customer/', CustomerAppViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).create_view, name='add customer'),

    path('show-customer/<int:pk>/<slug:slug>/', CustomerAppViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).show_view, name='show customer'),

    path('edit-customer/<int:pk>/<slug:slug>/', CustomerAppViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).edit_view, name='edit customer'),

    path('delete-customer/<int:pk>/<slug:slug>/', CustomerAppViews(
        template_list, redirect_url, form_list, Customer, files_are_used
    ).delete_view, name='delete customer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
