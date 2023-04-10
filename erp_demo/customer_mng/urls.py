from django.urls import path, include

from erp_demo.customer_mng.views import CustomerAppViews


urlpatterns = [
    path('', CustomerAppViews().customer_mng_index, name='customer mng index'),
    path('customer-list/', CustomerAppViews().customer_list, name='customer list'),
    path('add-customer/', CustomerAppViews().add_customer, name='add customer'),
    path('show-customer/<int:pk>/<slug:slug>/', CustomerAppViews().show_customer, name='show customer'),
    path('edit-customer/<int:pk>/<slug:slug>/', CustomerAppViews().edit_customer, name='edit customer'),
    path('delete-customer/<int:pk>/<slug:slug>/', CustomerAppViews().delete_customer, name='delete customer'),
]
