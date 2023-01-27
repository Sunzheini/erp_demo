from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from erp_demo.dox_mng.views import DoxMngViews


urlpatterns = [
    path('', DoxMngViews().dox_mng_index, name='dox mng index'),
    path('document-list/', DoxMngViews().document_list, name='document list'),
    path('add-document/', DoxMngViews().add_document, name='add document'),
    path('edit-document/<int:pk>/<slug:slug>/', DoxMngViews().edit_document, name='edit document'),
    path('delete-document/<int:pk>/<slug:slug>/', DoxMngViews().delete_document, name='delete document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
