from django.urls import path, include

from erp_demo.kpi_mng.forms import KpiForm, KpiViewForm, KpiEditForm, KpiDeleteForm
from erp_demo.kpi_mng.models import Kpi
from erp_demo.kpi_mng.views import KpiMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'kpi_mng/kpi_mng_index.html',
    'kpi_mng/kpi_list.html',
    'kpi_mng/add_kpi.html',
    'kpi_mng/show_kpi.html',
    'kpi_mng/edit_kpi.html',
    'kpi_mng/delete_kpi.html',
]

redirect_url = 'kpi list'

form_list = [
    # Create, View, Edit, Delete
    KpiForm, KpiViewForm, KpiEditForm, KpiDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', KpiMngViews(
        template_list, redirect_url, form_list, Kpi, files_are_used
    ).index_view, name='kpi mng index'),

    path('kpi-list/', KpiMngViews(
        template_list, redirect_url, form_list, Kpi, files_are_used
    ).list_view, name='kpi list'),

    path('add-kpi/', KpiMngViews(
        template_list, redirect_url, form_list, Kpi, files_are_used
    ).create_view, name='add kpi'),

    path('show-kpi/<int:pk>/<slug:slug>/', KpiMngViews(
        template_list, redirect_url, form_list, Kpi, files_are_used
    ).show_view, name='show kpi'),

    path('edit-kpi/<int:pk>/<slug:slug>/', KpiMngViews(
        template_list, redirect_url, form_list, Kpi, files_are_used
    ).edit_view, name='edit kpi'),

    path('delete-kpi/<int:pk>/<slug:slug>/', KpiMngViews(
        template_list, redirect_url, form_list, Kpi, files_are_used
    ).delete_view, name='delete kpi'),

    path('kpi-matrix/', KpiMngViews(
        template_list, redirect_url, form_list, Kpi, files_are_used
    ).kpi_matrix, name='kpi matrix'),
]
