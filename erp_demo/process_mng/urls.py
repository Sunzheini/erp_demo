from django.urls import path, include

# from erp_demo.process_mng.views import ProcessMngViews, ProcessMngIndexView
from erp_demo.process_mng.views import ProcessMngViews

urlpatterns = [
    path('', ProcessMngViews().process_mng_index, name='process mng index'),
    # path('', ProcessMngIndexView.as_view(), name='process mng index'),

    path('show-process-step/<int:pk>/<slug:slug>/', ProcessMngViews().show_process_step, name='show process step'),
    path('edit-process-step/<int:pk>/<slug:slug>/', ProcessMngViews().edit_process_step, name='edit process step'),
    path('delete-process-step/<int:pk>/<slug:slug>/', ProcessMngViews().delete_process_step, name='delete process step'),
    path('create-flowchart/<int:pk>/', ProcessMngViews().create_flowchart, name='create flowchart'),
    path('create-turtle/<int:pk>/', ProcessMngViews().create_turtle, name='create turtle'),
    path('process-map/', ProcessMngViews().create_process_map, name='create process map'),

    path('show-process/<int:pk>/<slug:slug>/', ProcessMngViews().show_process, name='show process'),
    path('edit-process/<int:pk>/<slug:slug>/', ProcessMngViews().edit_process, name='edit proces'),
    path('delete-process/<int:pk>/<slug:slug>/', ProcessMngViews().delete_process, name='delete process'),
]
