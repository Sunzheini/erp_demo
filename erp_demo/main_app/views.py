from django.shortcuts import render, redirect

from erp_demo.hr_mng.models import Employee
from erp_demo.main_app.forms import ManageDbHRForm, \
    ManageDbAllForm, DeleteDatabaseForm, \
    RequirementsForm, RequirementsEditForm, RequirementsDeleteForm

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.main_app.models import CaptainsLog, Requirements
from erp_demo.process_mng.models import Process


class MainAppViews:

    @staticmethod
    def index(request):
        context = {}
        return render(request, 'index.html', context)

    @staticmethod
    def organigramm(request):
        context = {
            'employees_w_owned_processes': SupportFunctions.get_owned_processes_list(Employee, Process),
        }
        return render(request, 'core/organigramm.html', context)

    @staticmethod
    def manage_db(request):
        context = {}
        return render(request, 'core/manage_db.html', context)

    @staticmethod
    def manage_db_all(request):
        template = 'core/manage_db_all.html'
        message = None
        message2 = None

        if 'button_delete_db' in request.POST:
            form = DeleteDatabaseForm(request.POST)
            if form.is_valid():
                message = SupportFunctions.delete_database()
                form = DeleteDatabaseForm()
            form2 = ManageDbAllForm()

        elif 'button_manage_db_all' in request.POST:
            form2 = ManageDbAllForm(request.POST, request.FILES)
            if form2.is_valid():
                message2 = SupportFunctions.recreate_database(request.FILES)
                form2 = ManageDbAllForm()
            form = DeleteDatabaseForm()

        else:
            form = DeleteDatabaseForm()
            form2 = ManageDbAllForm()

        context = {
            'form': form,
            'form2': form2,
            'message': message,
            'message2': message2,
        }
        return render(request, template, context)

    @staticmethod
    def logs(request):
        context = {
            'logs': CaptainsLog.objects.all(),
        }
        return render(request, 'core/logs.html', context)

    @staticmethod
    def my_tasks(request):
        context = {
            'tasks': CaptainsLog.objects.all(),
        }
        return render(request, 'core/my_tasks.html', context)

    @staticmethod
    def requirements_matrix(request):
        if 'button1' in request.POST:
            requirement_form = RequirementsForm(request.POST)
            if requirement_form.is_valid():
                requirement_form.save()
                requirement_form = RequirementsForm()
        else:
            requirement_form = RequirementsForm()

        context = {
            'requirement_form': requirement_form,
            'requirements': Requirements.objects.all(),
        }
        return render(request, 'core/requirements_matrix.html', context)

    @staticmethod
    def show_requirement(request, pk, slug):
        template = 'core/show_requirement.html'
        current_requirement = Requirements.objects.filter(pk=pk).get()
        context = {
            'requirement': current_requirement,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def edit_requirement(request, pk, slug):
        template = 'core/edit_requirement.html'
        current_requirement = Requirements.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = RequirementsEditForm(instance=current_requirement)
        else:
            form = RequirementsEditForm(request.POST, instance=current_requirement)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Edited a requirement `{output}`")
                return redirect('requirements matrix')
        context = {
            'form': form,
            'requirement': current_requirement,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def delete_requirement(request, pk, slug):
        template = 'core/delete_requirement.html'
        current_requirement = Requirements.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = RequirementsDeleteForm(instance=current_requirement)
        else:
            form = RequirementsDeleteForm(request.POST, instance=current_requirement)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Deleted a requirement `{output}`")
                return redirect('requirements matrix')
        context = {
            'form': form,
            'requirement': current_requirement,
        }
        return render(request, template, context)

