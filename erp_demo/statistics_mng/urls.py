from django.urls import path, include

from erp_demo.statistics_mng.forms import StatModel1Form, StatModel1ViewForm, StatModel1EditForm, StatModel1DeleteForm
from erp_demo.statistics_mng.models import StatModel1
from erp_demo.statistics_mng.views import StatisticsMngViews, StatModel1Views

# Set-up
# ----------------------------------------------------------------------------------

template_list_statistics = [
    'statistics_mng/statistics_mng_index.html',
    None,
    None,
    None,
    None,
    None,
]

template_list_stat_model1 = [
    'statistics_mng/stat_model1/stat_model1_index.html',
    'statistics_mng/stat_model1/stat_model1_list.html',
    'statistics_mng/stat_model1/add_stat_model1.html',
    'statistics_mng/stat_model1/show_stat_model1.html',
    'statistics_mng/stat_model1/edit_stat_model1.html',
    'statistics_mng/stat_model1/delete_stat_model1.html',
]

redirect_url_statistics = 'statistics mng index'

redirect_url_stat_model1 = 'stat model1 list'

form_list_statistics = [
    # Create, View, Edit, Delete
    None, None, None, None,
]

form_list_stat_model1 = [
    # Create, View, Edit, Delete
    StatModel1Form, StatModel1ViewForm, StatModel1EditForm, StatModel1DeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', StatisticsMngViews(
        template_list_statistics, redirect_url_statistics, form_list_statistics, None, files_are_used
    ).index_view, name='statistics mng index'),



    path('stat-model1/', StatModel1Views(
        template_list_stat_model1, redirect_url_stat_model1, form_list_stat_model1, StatModel1, files_are_used
    ).index_view, name='stat model1 index'),

    path('stat-model1/stat-model1-list/', StatModel1Views(
        template_list_stat_model1, redirect_url_stat_model1, form_list_stat_model1, StatModel1, files_are_used
    ).list_view, name='stat model1 list'),

    path('stat-model1/add-stat-model1/', StatModel1Views(
        template_list_stat_model1, redirect_url_stat_model1, form_list_stat_model1, StatModel1, files_are_used
    ).create_view, name='add stat model1'),

    path('stat-model1/show-stat-model1/<int:pk>/<slug:slug>/', StatModel1Views(
        template_list_stat_model1, redirect_url_stat_model1, form_list_stat_model1, StatModel1, files_are_used
    ).show_view, name='show stat model1'),

    path('stat-model1/edit-stat-model1/<int:pk>/<slug:slug>/', StatModel1Views(
        template_list_stat_model1, redirect_url_stat_model1, form_list_stat_model1, StatModel1, files_are_used
    ).edit_view, name='edit stat model1'),

    path('stat-model1/delete-stat-model1/<int:pk>/<slug:slug>/', StatModel1Views(
        template_list_stat_model1, redirect_url_stat_model1, form_list_stat_model1, StatModel1, files_are_used
    ).delete_view, name='delete stat model1'),
]
