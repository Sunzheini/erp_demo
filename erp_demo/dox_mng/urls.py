from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include

from erp_demo.dox_mng.views import DoxMngViews

from erp_demo.dox_mng.forms import DocumentForm, DocumentEditForm, DocumentDeleteForm
from erp_demo.dox_mng.models import Document

# Set-up
# ----------------------------------------------------------------------------------

template_list = [
    'dox_mng/dox_mng_index.html',
    'dox_mng/document_list.html',
    'dox_mng/add_document.html',
    'dox_mng/show_document.html',
    'dox_mng/edit_document.html',
    'dox_mng/delete_document.html',
]

redirect_url = 'document list'

form_list = [
    # Create, View, Edit, Delete
    DocumentForm, DocumentForm, DocumentEditForm, DocumentDeleteForm,
]

files_are_used = True

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', DoxMngViews(
        template_list, redirect_url, form_list, Document, files_are_used
    ).index_view, name='dox mng index'),

    path('document-list/', DoxMngViews(
        template_list, redirect_url, form_list, Document, files_are_used
    ).list_view, name='document list'),

    path('add-document/', DoxMngViews(
        template_list, redirect_url, form_list, Document, files_are_used
    ).create_view, name='add document'),

    path('show-document/<int:pk>/<slug:slug>/', DoxMngViews(
        template_list, redirect_url, form_list, Document, files_are_used
    ).show_view, name='show document'),

    path('edit-document/<int:pk>/<slug:slug>/', DoxMngViews(
        template_list, redirect_url, form_list, Document, files_are_used
    ).edit_view, name='edit document'),

    path('delete-document/<int:pk>/<slug:slug>/', DoxMngViews(
        template_list, redirect_url, form_list, Document, files_are_used
    ).delete_view, name='delete document'),

    # added for likes
    path('like/<int:pk>/', DoxMngViews(
        template_list, redirect_url, form_list, Document, files_are_used
    ).like_document, name='like document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
