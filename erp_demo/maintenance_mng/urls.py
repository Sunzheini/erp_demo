from django.urls import path, include

from erp_demo.maintenance_mng.forms import MachineForm, MachineViewForm, \
    MachineEditForm, MachineDeleteForm
from erp_demo.maintenance_mng.models import Machine
from erp_demo.maintenance_mng.views import MaintenanceMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'maintenance_mng/maintenance_mng_index.html',
    'maintenance_mng/maintenance_list.html',
    'maintenance_mng/add_maintenance.html',
    'maintenance_mng/show_maintenance.html',
    'maintenance_mng/edit_maintenance.html',
    'maintenance_mng/delete_maintenance.html',
]

redirect_url = 'maintenance list'

form_list = [
    # Create, View, Edit, Delete
    MachineForm, MachineViewForm, MachineEditForm, MachineDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', MaintenanceMngViews(
        template_list, redirect_url, form_list, Machine, files_are_used
    ).index_view, name='maintenance mng index'),

    path('machine-list/', MaintenanceMngViews(
        template_list, redirect_url, form_list, Machine, files_are_used
    ).list_view, name='maintenance list'),

    path('add-machine/', MaintenanceMngViews(
        template_list, redirect_url, form_list, Machine, files_are_used
    ).create_view, name='add maintenance'),

    path('show-machine/<int:pk>/<slug:slug>/', MaintenanceMngViews(
        template_list, redirect_url, form_list, Machine, files_are_used
    ).show_view, name='show maintenance'),

    path('edit-machine/<int:pk>/<slug:slug>/', MaintenanceMngViews(
        template_list, redirect_url, form_list, Machine, files_are_used
    ).edit_view, name='edit maintenance'),

    path('delete-machine/<int:pk>/<slug:slug>/', MaintenanceMngViews(
        template_list, redirect_url, form_list, Machine, files_are_used
    ).delete_view, name='delete maintenance'),
]
