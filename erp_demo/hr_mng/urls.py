from django.urls import path, include

from erp_demo.hr_mng.forms import EmployeeForm, EmployeeEditForm, EmployeeDeleteForm, \
    TrainingsForm, TrainingsEditForm, TrainingsDeleteForm, \
    PositionsForm, PositionsEditForm, PositionsDeleteForm
from erp_demo.hr_mng.models import Employee, Trainings, Positions
from erp_demo.hr_mng.views import HrMngViewsEmployees, HrMngViewsTrainings, HrMngViewsPositions

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

template_list_positions = [
    'hr_mng/position_index.html',
    'hr_mng/position_list.html',
    'hr_mng/add_position.html',
    'hr_mng/show_position.html',
    'hr_mng/edit_position.html',
    'hr_mng/delete_position.html',
]

redirect_url_employee = 'employee list'
redirect_url_trainings = 'training list'
redirect_url_positions = 'position list'

form_list_employee = [
    # Create, View, Edit, Delete
    EmployeeForm, EmployeeForm, EmployeeEditForm, EmployeeDeleteForm,
]

form_list_trainings = [
    # Create, View, Edit, Delete
    TrainingsForm, TrainingsForm, TrainingsEditForm, TrainingsDeleteForm,
]

form_list_positions = [
    # Create, View, Edit, Delete
    PositionsForm, PositionsForm, PositionsEditForm, PositionsDeleteForm,
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

    path('position/', include([
        path('', HrMngViewsPositions(
            template_list_positions, redirect_url_positions, form_list_positions, Positions, files_are_used
        ).index_view, name='position index'),

        path('position-list/', HrMngViewsPositions(
            template_list_positions, redirect_url_positions, form_list_positions, Positions, files_are_used
        ).list_view, name='position list'),

        path('add-position/', HrMngViewsPositions(
            template_list_positions, redirect_url_positions, form_list_positions, Positions, files_are_used
        ).create_view, name='add position'),

        path('show-position/<int:pk>/<slug:slug>/', HrMngViewsPositions(
            template_list_positions, redirect_url_positions, form_list_positions, Positions, files_are_used
        ).show_view, name='show position'),

        path('edit-position/<int:pk>/<slug:slug>/', HrMngViewsPositions(
            template_list_positions, redirect_url_positions, form_list_positions, Positions, files_are_used
        ).edit_view, name='edit position'),

        path('delete-position/<int:pk>/<slug:slug>/', HrMngViewsPositions(
            template_list_positions, redirect_url_positions, form_list_positions, Positions, files_are_used
        ).delete_view, name='delete position'),

    ])),

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
