from django.urls import path, include

from erp_demo.opportunity_mng.forms import OpportunityForm, OpportunityViewForm, OpportunityEditForm, OpportunityDeleteForm
from erp_demo.opportunity_mng.models import Opportunity
from erp_demo.opportunity_mng.views import OpportunityMngViews

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'opportunity_mng/opportunity_mng_index.html',
    'opportunity_mng/opportunity_list.html',
    'opportunity_mng/add_opportunity.html',
    'opportunity_mng/show_opportunity.html',
    'opportunity_mng/edit_opportunity.html',
    'opportunity_mng/delete_opportunity.html',
]

redirect_url = 'opportunity list'

form_list = [
    # Create, View, Edit, Delete
    OpportunityForm, OpportunityViewForm, OpportunityEditForm, OpportunityDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', OpportunityMngViews(
        template_list, redirect_url, form_list, Opportunity, files_are_used
    ).index_view, name='opportunity mng index'),

    path('opportunity-list/', OpportunityMngViews(
        template_list, redirect_url, form_list, Opportunity, files_are_used
    ).list_view, name='opportunity list'),

    path('add-opportunity/', OpportunityMngViews(
        template_list, redirect_url, form_list, Opportunity, files_are_used
    ).create_view, name='add opportunity'),

    path('show-opportunity/<int:pk>/<slug:slug>/', OpportunityMngViews(
        template_list, redirect_url, form_list, Opportunity, files_are_used
    ).show_view, name='show opportunity'),

    path('edit-opportunity/<int:pk>/<slug:slug>/', OpportunityMngViews(
        template_list, redirect_url, form_list, Opportunity, files_are_used
    ).edit_view, name='edit opportunity'),

    path('delete-opportunity/<int:pk>/<slug:slug>/', OpportunityMngViews(
        template_list, redirect_url, form_list, Opportunity, files_are_used
    ).delete_view, name='delete opportunity'),
]
