from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from erp_demo.characteristics_mng.views import CharacteristicAppViews

from erp_demo.characteristics_mng.forms import CharacteristicForm, CharacteristicEditForm, \
    CharacteristicDeleteForm, CharacteristicViewForm
from erp_demo.characteristics_mng.models import Characteristic

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'characteristics_mng/characteristics_mng_index.html',
    'characteristics_mng/characteristics_list.html',
    'characteristics_mng/add_characteristic.html',
    'characteristics_mng/show_characteristic.html',
    'characteristics_mng/edit_characteristic.html',
    'characteristics_mng/delete_characteristic.html',
]

redirect_url = 'characteristic list'

form_list = [
    # Create, View, Edit, Delete
    CharacteristicForm, CharacteristicViewForm, CharacteristicEditForm, CharacteristicDeleteForm,
]

files_are_used = True

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', CharacteristicAppViews(
        template_list, redirect_url, form_list, Characteristic, files_are_used
    ).index_view, name='characteristic mng index'),

    path('characteristic-list/', CharacteristicAppViews(
        template_list, redirect_url, form_list, Characteristic, files_are_used
    ).list_view, name='characteristic list'),

    path('add-characteristic/', CharacteristicAppViews(
        template_list, redirect_url, form_list, Characteristic, files_are_used
    ).create_view, name='add characteristic'),

    path('show-characteristic/<int:pk>/<slug:slug>/', CharacteristicAppViews(
        template_list, redirect_url, form_list, Characteristic, files_are_used
    ).show_view, name='show characteristic'),

    path('edit-characteristic/<int:pk>/<slug:slug>/', CharacteristicAppViews(
        template_list, redirect_url, form_list, Characteristic, files_are_used
    ).edit_view, name='edit characteristic'),

    path('delete-characteristic/<int:pk>/<slug:slug>/', CharacteristicAppViews(
        template_list, redirect_url, form_list, Characteristic, files_are_used
    ).delete_view, name='delete characteristic'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
