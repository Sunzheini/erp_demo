from django.urls import path, include

from erp_demo.calibration_mng.forms import MeasuringEquipmentForm, MeasuringEquipmentShowForm, \
    MeasuringEquipmentEditForm, MeasuringEquipmentDeleteForm
from erp_demo.calibration_mng.models import MeasuringEquipment
from erp_demo.calibration_mng.views import CalibrationMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'calibration_mng/calibration_mng_index.html',
    'calibration_mng/calibration_list.html',
    'calibration_mng/add_calibration.html',
    'calibration_mng/show_calibration.html',
    'calibration_mng/edit_calibration.html',
    'calibration_mng/delete_calibration.html',
]

redirect_url = 'calibration list'

form_list = [
    # Create, View, Edit, Delete
    MeasuringEquipmentForm, MeasuringEquipmentShowForm, MeasuringEquipmentEditForm, MeasuringEquipmentDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', CalibrationMngViews(
        template_list, redirect_url, form_list, MeasuringEquipment, files_are_used
    ).index_view, name='calibration mng index'),

    path('calibration-list/', CalibrationMngViews(
        template_list, redirect_url, form_list, MeasuringEquipment, files_are_used
    ).list_view, name='calibration list'),

    path('add-calibration/', CalibrationMngViews(
        template_list, redirect_url, form_list, MeasuringEquipment, files_are_used
    ).create_view, name='add calibration'),

    path('show-calibration/<int:pk>/<slug:slug>/', CalibrationMngViews(
        template_list, redirect_url, form_list, MeasuringEquipment, files_are_used
    ).show_view, name='show calibration'),

    path('edit-calibration/<int:pk>/<slug:slug>/', CalibrationMngViews(
        template_list, redirect_url, form_list, MeasuringEquipment, files_are_used
    ).edit_view, name='edit calibration'),

    path('delete-calibration/<int:pk>/<slug:slug>/', CalibrationMngViews(
        template_list, redirect_url, form_list, MeasuringEquipment, files_are_used
    ).delete_view, name='delete calibration'),
]
