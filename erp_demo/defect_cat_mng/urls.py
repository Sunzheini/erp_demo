from django.urls import path, include

from erp_demo.defect_cat_mng.forms import DefectCatalogueForm, DefectCatalogueEditForm, \
    DefectCatalogueDeleteForm
from erp_demo.defect_cat_mng.models import DefectCatalogue
from erp_demo.defect_cat_mng.views import DefectCatMngViews


# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'defect_cat_mng/defect_cat_mng_index.html',
    'defect_cat_mng/defect_cat_list.html',
    'defect_cat_mng/add_defect_cat.html',
    'defect_cat_mng/show_defect_cat.html',
    'defect_cat_mng/edit_defect_cat.html',
    'defect_cat_mng/delete_defect_cat.html',
]

redirect_url = 'defect cat list'

form_list = [
    # Create, View, Edit, Delete
    DefectCatalogueForm, DefectCatalogueForm, DefectCatalogueEditForm, DefectCatalogueDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', DefectCatMngViews(
        template_list, redirect_url, form_list, DefectCatalogue, files_are_used
    ).index_view, name='defect cat mng index'),

    path('defect-cat-list/', DefectCatMngViews(
        template_list, redirect_url, form_list, DefectCatalogue, files_are_used
    ).list_view, name='defect cat list'),

    path('add-defect-cat/', DefectCatMngViews(
        template_list, redirect_url, form_list, DefectCatalogue, files_are_used
    ).create_view, name='add defect cat'),

    path('show-defect-cat/<int:pk>/<slug:slug>/', DefectCatMngViews(
        template_list, redirect_url, form_list, DefectCatalogue, files_are_used
    ).show_view, name='show defect cat'),

    path('edit-defect-cat/<int:pk>/<slug:slug>/', DefectCatMngViews(
        template_list, redirect_url, form_list, DefectCatalogue, files_are_used
    ).edit_view, name='edit defect cat'),

    path('delete-defect-cat/<int:pk>/<slug:slug>/', DefectCatMngViews(
        template_list, redirect_url, form_list, DefectCatalogue, files_are_used
    ).delete_view, name='delete defect cat'),
]
