from django.urls import path, include

from erp_demo.hr_mng.forms import EmployeeForm, EmployeeEditForm, EmployeeDeleteForm, \
    TrainingsForm, TrainingsEditForm, TrainingsDeleteForm
from erp_demo.hr_mng.models import Employee, Trainings
from erp_demo.hr_mng.views import HrMngViewsEmployees, HrMngViewsTrainings

# Set-up
# ----------------------------------------------------------------------------------

template_list_employee = [
    'hr_mng/hr_mng_index.html',
    'hr_mng/employee_list.html',
    'hr_mng/add_employee.html',
    'hr_mng/show_employee.html',
    'hr_mng/edit_employee.html',
    'hr_mng/delete_employee.html',
]

template_list_trainings = [
    'hr_mng/training_index.html',
    'hr_mng/training_list.html',
    'hr_mng/add_training.html',
    'hr_mng/show_training.html',
    'hr_mng/edit_training.html',
    'hr_mng/delete_training.html',
]

redirect_url_employee = 'employee list'
redirect_url_trainings = 'training list'

form_list_employee = [
    # Create, View, Edit, Delete
    EmployeeForm, EmployeeForm, EmployeeEditForm, EmployeeDeleteForm,
]

form_list_trainings = [
    # Create, View, Edit, Delete
    TrainingsForm, TrainingsForm, TrainingsEditForm, TrainingsDeleteForm,
]

files_are_used = False

# ----------------------------------------------------------------------------------

urlpatterns = [
    path('', HrMngViewsEmployees(
        template_list_employee, redirect_url_employee, form_list_employee, Employee, files_are_used
    ).index_view, name='hr mng index'),

    path('employee-list/', HrMngViewsEmployees(
        template_list_employee, redirect_url_employee, form_list_employee, Employee, files_are_used
    ).list_view, name='employee list'),

    path('add-employee/', HrMngViewsEmployees(
        template_list_employee, redirect_url_employee, form_list_employee, Employee, files_are_used
    ).create_view, name='add employee'),

    path('show-employee/<int:pk>/<slug:slug>/', HrMngViewsEmployees(
        template_list_employee, redirect_url_employee, form_list_employee, Employee, files_are_used
    ).show_view, name='show employee'),

    path('edit-employee/<int:pk>/<slug:slug>/', HrMngViewsEmployees(
        template_list_employee, redirect_url_employee, form_list_employee, Employee, files_are_used
    ).edit_view, name='edit employee'),

    path('delete-employee/<int:pk>/<slug:slug>/', HrMngViewsEmployees(
        template_list_employee, redirect_url_employee, form_list_employee, Employee, files_are_used
    ).delete_view, name='delete employee'),



    path('training/', include([
        path('', HrMngViewsTrainings(
        template_list_trainings, redirect_url_trainings, form_list_trainings, Trainings, files_are_used
    ).index_view, name='training index'),

        path('training-list/', HrMngViewsTrainings(
        template_list_trainings, redirect_url_trainings, form_list_trainings, Trainings, files_are_used
    ).list_view, name='training list'),

        path('add-training/', HrMngViewsTrainings(
        template_list_trainings, redirect_url_trainings, form_list_trainings, Trainings, files_are_used
    ).create_view, name='add training'),

        path('show-training/<int:pk>/<slug:slug>/', HrMngViewsTrainings(
        template_list_trainings, redirect_url_trainings, form_list_trainings, Trainings, files_are_used
    ).show_view, name='show training'),

        path('edit-training/<int:pk>/<slug:slug>/', HrMngViewsTrainings(
        template_list_trainings, redirect_url_trainings, form_list_trainings, Trainings, files_are_used
    ).edit_view, name='edit training'),

        path('delete-training/<int:pk>/<slug:slug>/', HrMngViewsTrainings(
        template_list_trainings, redirect_url_trainings, form_list_trainings, Trainings, files_are_used
    ).delete_view, name='delete training'),

        path('training-matrix/', HrMngViewsTrainings(
        template_list_trainings, redirect_url_trainings, form_list_trainings, Trainings, files_are_used
    ).training_matrix, name='training matrix'),
    ])),
]
