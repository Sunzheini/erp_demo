from django.urls import path, include

from erp_demo.supplier_mng.forms import SupplierForm, SupplierViewForm, SupplierEditForm, SupplierDeleteForm, \
    MaterialForm, MaterialViewForm, MaterialEditForm, MaterialDeleteForm
from erp_demo.supplier_mng.models import Supplier, Material
from erp_demo.supplier_mng.views import SupplierMngViews, MaterialMngViews


# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'supplier_mng/supplier_mng_index.html',
    'supplier_mng/supplier_list.html',
    'supplier_mng/add_supplier.html',
    'supplier_mng/show_supplier.html',
    'supplier_mng/edit_supplier.html',
    'supplier_mng/delete_supplier.html',
]

template_list_materials = [
    'supplier_mng/materials_index.html',
    'supplier_mng/materials_list.html',
    'supplier_mng/add_material.html',
    'supplier_mng/show_material.html',
    'supplier_mng/edit_material.html',
    'supplier_mng/delete_material.html',
]

redirect_url = 'supplier list'
redirect_url_materials = 'materials list'

form_list = [
    # Create, View, Edit, Delete
    SupplierForm, SupplierViewForm, SupplierEditForm, SupplierDeleteForm,
]

form_list_materials = [
    # Create, View, Edit, Delete
    MaterialForm, MaterialViewForm, MaterialEditForm, MaterialDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', SupplierMngViews(
        template_list, redirect_url, form_list, Supplier, files_are_used
    ).index_view, name='supplier mng index'),

    path('supplier-list/', SupplierMngViews(
        template_list, redirect_url, form_list, Supplier, files_are_used
    ).list_view, name='supplier list'),

    path('add-supplier/', SupplierMngViews(
        template_list, redirect_url, form_list, Supplier, files_are_used
    ).create_view, name='add supplier'),

    path('show-supplier/<int:pk>/<slug:slug>/', SupplierMngViews(
        template_list, redirect_url, form_list, Supplier, files_are_used
    ).show_view, name='show supplier'),

    path('edit-supplier/<int:pk>/<slug:slug>/', SupplierMngViews(
        template_list, redirect_url, form_list, Supplier, files_are_used
    ).edit_view, name='edit supplier'),

    path('delete-supplier/<int:pk>/<slug:slug>/', SupplierMngViews(
        template_list, redirect_url, form_list, Supplier, files_are_used
    ).delete_view, name='delete supplier'),


    path('supplier-scores', SupplierMngViews(
        template_list, redirect_url, form_list, Supplier, files_are_used
    ).supplier_scores, name='supplier scores'),


    path('materials/', MaterialMngViews(
        template_list_materials, redirect_url_materials, form_list_materials, Material, files_are_used
    ).index_view, name='material mng index'),

    path('materials-list/', MaterialMngViews(
        template_list_materials, redirect_url_materials, form_list_materials, Material, files_are_used
    ).list_view, name='materials list'),

    path('add-material/', MaterialMngViews(
        template_list_materials, redirect_url_materials, form_list_materials, Material, files_are_used
    ).create_view, name='add material'),

    path('show-material/<int:pk>/<slug:slug>/', MaterialMngViews(
        template_list_materials, redirect_url_materials, form_list_materials, Material, files_are_used
    ).show_view, name='show material'),

    path('edit-material/<int:pk>/<slug:slug>/', MaterialMngViews(
        template_list_materials, redirect_url_materials, form_list_materials, Material, files_are_used
    ).edit_view, name='edit material'),

    path('delete-material/<int:pk>/<slug:slug>/', MaterialMngViews(
        template_list_materials, redirect_url_materials, form_list_materials, Material, files_are_used
    ).delete_view, name='delete material'),
]
