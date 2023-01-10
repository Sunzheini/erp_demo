from django.urls import path, include

from erp_demo.process_mng.views import ProcessMngViews


urlpatterns = [
    path('', ProcessMngViews().process_mng_index, name='process mng index'),
]
