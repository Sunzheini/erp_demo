from django.shortcuts import render, redirect

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.hr_mng.forms import EmployeeForm, EmployeeEditForm, \
    EmployeeDeleteForm, EmployeePositionForm, \
    TrainingsForm, TrainingsEditForm, TrainingsDeleteForm
from erp_demo.hr_mng.models import Employee, Trainings


class HrMngViews:
    @staticmethod
    def hr_mng_index(request):
        context = {}
        return render(request, 'hr_mng/hr_mng_index.html', context)

    @staticmethod
    def employee_list(request):     # ToDo: cache
        template = 'hr_mng/employee_list.html'

        table = Employee
        column_name = 'position'
        choice = None

        if request.method == 'GET':
            form = EmployeePositionForm()
        else:
            form = EmployeePositionForm(request.POST)
            if form.is_valid():
                choice = form.cleaned_data['employee_position_dropdown']

        context = {
            'all_objects': SupportFunctions.extract_entry_by_choice(table, column_name, choice),
            'choice_form': form,
        }
        return render(request, template, context)

    @staticmethod
    def add_employee(request):
        template = 'hr_mng/add_employee.html'
        if request.method == 'GET':
            form = EmployeeForm()
        else:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('employee list')
        context = {
            'form': form,
        }
        return render(request, template, context)

    @staticmethod
    def edit_employee(request, pk, slug):
        template = 'hr_mng/edit_employee.html'
        current_employee = Employee.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = EmployeeEditForm(instance=current_employee)
        else:
            form = EmployeeEditForm(request.POST, instance=current_employee)
            if form.is_valid():
                form.save()
                return redirect('employee list')
        context = {
            'form': form,
            'employee': current_employee,
        }
        return render(request, template, context)

    @staticmethod
    def delete_employee(request, pk, slug):
        template = 'hr_mng/delete_employee.html'
        current_employee = Employee.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = EmployeeDeleteForm(instance=current_employee)
        else:
            form = EmployeeDeleteForm(request.POST, instance=current_employee)
            if form.is_valid():
                form.save()
                return redirect('employee list')
        context = {
            'form': form,
            'employee': current_employee,
        }
        return render(request, template, context)

    # Trainings
    #  ---------------------------------------------------------------------------------------

    @staticmethod
    def training_index(request):
        context = {}
        return render(request, 'hr_mng/training_index.html', context)

    @staticmethod
    def training_list(request):
        template = 'hr_mng/training_list.html'
        context = {
            'all_objects': Trainings.objects.all(),
        }
        return render(request, template, context)

    @staticmethod
    def add_training(request):
        template = 'hr_mng/add_training.html'
        if request.method == 'GET':
            form = TrainingsForm()
        else:
            form = TrainingsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('training list')
        context = {
            'form': form,
        }
        return render(request, template, context)

    @staticmethod
    def edit_training(request, pk, slug):
        template = 'hr_mng/edit_training.html'
        current_training = Trainings.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = TrainingsEditForm(instance=current_training)
        else:
            form = TrainingsEditForm(request.POST, instance=current_training)
            if form.is_valid():
                form.save()
                return redirect('training list')
        context = {
            'form': form,
            'training': current_training,
        }
        return render(request, template, context)

    @staticmethod
    def delete_training(request, pk, slug):
        template = 'hr_mng/delete_training.html'
        current_training = Trainings.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = TrainingsDeleteForm(instance=current_training)
        else:
            form = TrainingsDeleteForm(request.POST, instance=current_training)
            if form.is_valid():
                form.save()
                return redirect('training list')
        context = {
            'form': form,
            'training': current_training,
        }
        return render(request, template, context)

    @staticmethod
    def training_matrix(request):
        context = {}
        return render(request, 'hr_mng/training_matrix.html', context)
