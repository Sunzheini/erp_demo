from django.shortcuts import render, redirect

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.hr_mng.forms import EmployeeForm, EmployeeEditForm, \
    EmployeeDeleteForm, EmployeePositionForm
from erp_demo.hr_mng.models import Employee


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
