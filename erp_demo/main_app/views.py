from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login     # users and login

from erp_demo.dox_mng.models import Document, DocumentEditPurgatory
from erp_demo.hr_mng.models import Employee
from erp_demo.main_app.forms import ManageDbHRForm, \
    ManageDbAllForm, DeleteDatabaseForm, \
    RequirementsForm, RequirementsEditForm, RequirementsDeleteForm, \
    SearchForm

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.main_app.models import CaptainsLog, Requirements
from erp_demo.process_mng.models import Process


"""
Creation of login
superuser: daniel, daniel_zorov@abv.bg, Maimun06
+1:10:00: create User model
+1:39:00: user = User.objects.create_user(
		username='maxi',
		password='Maimun04',
	)
+1:52:00: login(request, user)  # creates session, attaches user to req, logs in user
          logout...  # deletes session, ...

can and should change user permissions in django admin, can also make groups


	
	
"""


class MainAppViews:
    @staticmethod
    def index(request):

# --------------------------------------------------------

        # prints the username if ok else None
        print(authenticate(username='daniel', password='Maimun06'))

# --------------------------------------------------------

        search_pattern = None
        info_to_display = None
        if request.method == 'GET':
            form = SearchForm()
        else:
            form = SearchForm(request.POST)
            if form.is_valid():
                search_pattern = form.cleaned_data['form_keyword']
                choice = form.cleaned_data['search_type_dropdown']
                info_to_display = SupportFunctions.search_results(search_pattern, choice)
                form = SearchForm()
        context = {
            'search_form': form,
            'info_to_display': info_to_display,
            'info': search_pattern,
        }
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
    def favorites(request):
        context = {
            'favorites': Document.objects.filter(is_liked_by_user=True),
        }
        return render(request, 'core/favorites.html', context)

    @staticmethod
    def my_tasks(request):
        template = 'core/my_tasks.html'
        all_objects = DocumentEditPurgatory.objects.all()
        context = {
            'all_objects': all_objects,
        }
        return render(request, template, context)

    @staticmethod
    def approve_revision(request, pk, slug):
        current_revision = DocumentEditPurgatory.objects.filter(pk=pk).get()
        SupportFunctions.approve_and_upload_revision(current_revision)
        return redirect('my tasks')

    @staticmethod
    def delete_revision(request, pk, slug):
        current_revision = DocumentEditPurgatory.objects.filter(pk=pk).get()
        current_revision.delete()
        return redirect('my tasks')

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

