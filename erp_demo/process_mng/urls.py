from django.urls import path, include

from erp_demo.process_mng.views import ProcessMngViews


urlpatterns = [
    path('', ProcessMngViews().process_mng_index, name='process mng index'),
    path('edit-process-step/<int:pk>/<slug:slug>/', ProcessMngViews().edit_process_step, name='edit process step'),
    path('delete-process-step/<int:pk>/<slug:slug>/', ProcessMngViews().delete_process_step, name='delete process step'),
]
