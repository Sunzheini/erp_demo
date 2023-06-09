from django.urls import path, include

from erp_demo.nonconformity_mng.forms import NonconformityForm, NonconformityViewForm, NonconformityEditForm, NonconformityDeleteForm
from erp_demo.nonconformity_mng.models import Nonconformity
from erp_demo.nonconformity_mng.views import NonconformityMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'nonconformity_mng/nonconformity_mng_index.html',
    'nonconformity_mng/nonconformity_list.html',
    'nonconformity_mng/add_nonconformity.html',
    'nonconformity_mng/show_nonconformity.html',
    'nonconformity_mng/edit_nonconformity.html',
    'nonconformity_mng/delete_nonconformity.html',
]

redirect_url = 'nonconformity list'

form_list = [
    # Create, View, Edit, Delete
    NonconformityForm, NonconformityViewForm, NonconformityEditForm, NonconformityDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', NonconformityMngViews(
        template_list, redirect_url, form_list, Nonconformity, files_are_used
    ).index_view, name='nonconformity mng index'),

    path('nonconformity-list/', NonconformityMngViews(
        template_list, redirect_url, form_list, Nonconformity, files_are_used
    ).list_view, name='nonconformity list'),

    path('add-nonconformity/', NonconformityMngViews(
        template_list, redirect_url, form_list, Nonconformity, files_are_used
    ).create_view, name='add nonconformity'),

    path('show-nonconformity/<int:pk>/<slug:slug>/', NonconformityMngViews(
        template_list, redirect_url, form_list, Nonconformity, files_are_used
    ).show_view, name='show nonconformity'),

    path('edit-nonconformity/<int:pk>/<slug:slug>/', NonconformityMngViews(
        template_list, redirect_url, form_list, Nonconformity, files_are_used
    ).edit_view, name='edit nonconformity'),

    path('delete-nonconformity/<int:pk>/<slug:slug>/', NonconformityMngViews(
        template_list, redirect_url, form_list, Nonconformity, files_are_used
    ).delete_view, name='delete nonconformity'),


    path('write-to-excel/<int:pk>/<slug:slug>/', NonconformityMngViews(
        template_list, redirect_url, form_list, Nonconformity, files_are_used
    ).write_to_excel, name='write to excel'),
]
