from django.urls import path
from erp_demo.analytics.forms import AnalysisForm, AnalysisEditForm, AnalysisDeleteForm, AnalysisViewForm
from erp_demo.analytics.models import Analysis
from erp_demo.analytics.views import AnalysisMngViews


# Set-up
# ----------------------------------------------------------------------------------

template_list_analysis = [
    'analytics/analysis_mng_index.html',
    'analytics/analysis_list.html',
    'analytics/add_analysis.html',
    'analytics/show_analysis.html',
    'analytics/edit_analysis.html',
    'analytics/delete_analysis.html',
]

redirect_url_analysis = 'analysis list'

form_list_analysis = [
    # Create, View, Edit, Delete
    AnalysisForm, AnalysisViewForm, AnalysisEditForm, AnalysisDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', AnalysisMngViews(
        template_list_analysis, redirect_url_analysis, form_list_analysis, Analysis, files_are_used
    ).index_view, name='analysis mng index'),

    path('analysis-list/', AnalysisMngViews(
        template_list_analysis, redirect_url_analysis, form_list_analysis, Analysis, files_are_used
    ).list_view, name='analysis list'),

    path('add-analysis/', AnalysisMngViews(
        template_list_analysis, redirect_url_analysis, form_list_analysis, Analysis, files_are_used
    ).create_view, name='add analysis'),

    path('show-analysis/<int:pk>/<slug:slug>/', AnalysisMngViews(
        template_list_analysis, redirect_url_analysis, form_list_analysis, Analysis, files_are_used
    ).show_view, name='show analysis'),

    path('edit-analysis/<int:pk>/<slug:slug>/', AnalysisMngViews(
        template_list_analysis, redirect_url_analysis, form_list_analysis, Analysis, files_are_used
    ).edit_view, name='edit analysis'),

    path('delete-analysis/<int:pk>/<slug:slug>/', AnalysisMngViews(
        template_list_analysis, redirect_url_analysis, form_list_analysis, Analysis, files_are_used
    ).delete_view, name='delete analysis'),
]
