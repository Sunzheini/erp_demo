from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from erp_demo.dox_mng.views import add_document, edit_document, delete_document, \
    document_list, dox_mng_index


urlpatterns = [
    path('', dox_mng_index, name='dox mng index'),
    path('document-list/', document_list, name='document list'),
    path('add-document/', add_document, name='add document'),
    path('edit_document/<int:pk>/<slug:slug>/', edit_document, name='edit document'),
    path('delete_document/<int:pk>/<slug:slug>/', delete_document, name='delete document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
