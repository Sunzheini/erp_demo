from django.urls import path, include

from erp_demo.process_mng.views import process_mng_index

urlpatterns = [
    path('', process_mng_index, name='process mng index'),
]
