from django.shortcuts import render

from erp_demo.custom_logic.custom_logic import SupportFunctions, DataManipulation
from erp_demo.hr_mng.forms import EmployeePositionForm
from erp_demo.hr_mng.models import Employee, Trainings
from erp_demo.custom_logic.custom_prototypes import PrototypeViews


class HrMngViewsEmployees(PrototypeViews):
    @SupportFunctions.login_check
    def list_view(self, request):
        self._empty_context()

        # new logic for the dropdown
        # ---------------------------------------------------------------------------------------
        table = Employee
        column_name = 'position'
        choice = None
        form = EmployeePositionForm()

        if request.method == 'GET':
            form = EmployeePositionForm()
        else:
            try:
                form = EmployeePositionForm(request.POST)
                if form.is_valid():
                    choice = form.cleaned_data['employee_position_dropdown']
            except Exception as e:
                print(f"Form processing error: {e}")
                form.add_error(None, "An error occurred during form processing.")

        all_objects = DataManipulation.data_after_choice_form(table, column_name, choice)

        self.context['all_objects'] = all_objects
        self.context['choice_form'] = form
        # ---------------------------------------------------------------------------------------

        try:
            return render(request, self.list_template, self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})


class HrMngViewsTrainings(PrototypeViews):
    @staticmethod
    @SupportFunctions.allow_groups()
    def training_matrix(request):
        all_objects = Trainings.objects.all()
        number_of_trainings = all_objects.count()

        context = {
            'all_objects': all_objects,
            'employees_w_their_trainings': DataManipulation.get_owned_trainings_list(Employee, Trainings),
            'number_of_trainings': number_of_trainings,
        }

        try:
            return render(request, 'hr_mng/training_matrix.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})
