from django.urls import path, include
from erp_demo.hr_mng.views import HrMngViews


urlpatterns = [
    path('', HrMngViews().hr_mng_index, name='hr mng index'),
    path('employee-list/', HrMngViews().employee_list, name='employee list'),
    path('add-employee/', HrMngViews().add_employee, name='add employee'),

    path('edit-employee/<int:pk>/<slug:slug>/', HrMngViews().edit_employee, name='edit employee'),
    path('delete-employee/<int:pk>/<slug:slug>/', HrMngViews().delete_employee, name='delete employee'),

    path('training/', include([
        path('', HrMngViews().training_index, name='training index'),
        path('training-list/', HrMngViews().training_list, name='training list'),
        path('add-training/', HrMngViews().add_training, name='add training'),
        path('training-matrix/', HrMngViews().training_matrix, name='training matrix'),

        path('edit-training/<int:pk>/<slug:slug>/', HrMngViews().edit_training, name='edit training'),
        path('delete-training/<int:pk>/<slug:slug>/', HrMngViews().delete_training, name='delete training'),
    ])),
]
