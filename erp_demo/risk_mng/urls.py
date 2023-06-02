from django.urls import path, include

from erp_demo.risk_mng.forms import RiskForm, RiskViewForm, RiskEditForm, RiskDeleteForm
from erp_demo.risk_mng.models import Risk
from erp_demo.risk_mng.views import RiskMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'risk_mng/risk_mng_index.html',
    'risk_mng/risk_list.html',
    'risk_mng/add_risk.html',
    'risk_mng/show_risk.html',
    'risk_mng/edit_risk.html',
    'risk_mng/delete_risk.html',
]

redirect_url = 'risk list'

form_list = [
    # Create, View, Edit, Delete
    RiskForm, RiskViewForm, RiskEditForm, RiskDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', RiskMngViews(
        template_list, redirect_url, form_list, Risk, files_are_used
    ).index_view, name='risk mng index'),

    path('risk-list/', RiskMngViews(
        template_list, redirect_url, form_list, Risk, files_are_used
    ).list_view, name='risk list'),

    path('add-risk/', RiskMngViews(
        template_list, redirect_url, form_list, Risk, files_are_used
    ).create_view, name='add risk'),

    path('show-risk/<int:pk>/<slug:slug>/', RiskMngViews(
        template_list, redirect_url, form_list, Risk, files_are_used
    ).show_view, name='show risk'),

    path('edit-risk/<int:pk>/<slug:slug>/', RiskMngViews(
        template_list, redirect_url, form_list, Risk, files_are_used
    ).edit_view, name='edit risk'),

    path('delete-risk/<int:pk>/<slug:slug>/', RiskMngViews(
        template_list, redirect_url, form_list, Risk, files_are_used
    ).delete_view, name='delete risk'),
]
