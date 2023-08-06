from django.shortcuts import render, redirect

from erp_demo.custom_logic.db_manipulation import DatabaseManipulation
from erp_demo.custom_logic.export_database import export_database
from erp_demo.dox_mng.models import Document, DocumentEditPurgatory
from erp_demo.hr_mng.models import Employee
from erp_demo.main_app.forms import ManageDbAllForm, DeleteDatabaseForm, \
    RequirementsForm, RequirementsEditForm, RequirementsDeleteForm, \
    SearchForm, RequirementsDocumentForm, ExportDatabaseForm

from erp_demo.custom_logic.custom_logic import SupportFunctions
from erp_demo.main_app.models import CaptainsLog, Requirements
from erp_demo.user_mng.models import AppUser


class MainAppViews:
    @staticmethod
    # @SupportFunctions.allow_groups(groups=['owners'])
    @SupportFunctions.allow_groups()
    def index(request):
        search_pattern = None
        info_to_display = None
        form = SearchForm()

        if request.method == 'GET':
            form = SearchForm()
        else:
            try:
                form = SearchForm(request.POST)
                if form.is_valid():
                    search_pattern = form.cleaned_data['form_keyword']
                    choice = form.cleaned_data['search_type_dropdown']
                    info_to_display = SupportFunctions.search_results(search_pattern, choice)
                    form = SearchForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                form.add_error(None, "An error occurred during form processing.")

        context = {
            'search_form': form,
            'info_to_display': info_to_display,
            'info': search_pattern,
        }

        try:
            return render(request, 'index.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def organigramm(request):
        try:
            all_objects = Employee.objects.all()
        except Employee.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Employee} not found."})

        context = {
            'all_objects': all_objects,
        }

        try:
            return render(request, 'core/organigramm.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def manage_db(request):
        context = {}

        try:
            return render(request, 'core/manage_db.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def manage_db_all(request):
        template = 'core/manage_db_all.html'
        message = None
        message2 = None
        message3 = None
        form = DeleteDatabaseForm()
        form2 = ManageDbAllForm()
        form3 = ExportDatabaseForm()

        if 'button_delete_db' in request.POST:
            try:
                form = DeleteDatabaseForm(request.POST)
                if form.is_valid():
                    message = DatabaseManipulation.delete_database()
                    form = DeleteDatabaseForm()
                form2 = ManageDbAllForm()
                form3 = ExportDatabaseForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                form.add_error(None, "An error occurred during form processing.")
                form2 = ManageDbAllForm()
                form3 = ExportDatabaseForm()

        elif 'button_manage_db_all' in request.POST:
            try:
                form2 = ManageDbAllForm(request.POST, request.FILES)
                if form2.is_valid():
                    message2 = DatabaseManipulation.recreate_database(request.FILES)
                    form2 = ManageDbAllForm()
                form = DeleteDatabaseForm()
                form3 = ExportDatabaseForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                form2.add_error(None, "An error occurred during form processing.")
                form = DeleteDatabaseForm()
                form3 = ExportDatabaseForm()

        elif 'button_export_db' in request.POST:
            try:
                form3 = ExportDatabaseForm(request.POST)
                if form3.is_valid():
                    message3 = export_database()
                    form3 = ExportDatabaseForm()
                form = DeleteDatabaseForm()
                form2 = ManageDbAllForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                form3.add_error(None, "An error occurred during form processing.")
                form = DeleteDatabaseForm()
                form2 = ManageDbAllForm()

        else:
            form = DeleteDatabaseForm()
            form2 = ManageDbAllForm()
            form3 = ExportDatabaseForm()

        context = {
            'form': form,
            'form2': form2,
            'form3': form3,
            'message': message,
            'message2': message2,
            'message3': message3,
            'users': AppUser.objects.all(),
        }

        try:
            return render(request, template, context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def logs(request):
        try:
            logs = CaptainsLog.objects.all()
        except CaptainsLog.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{CaptainsLog} not found."})

        context = {
            'logs': logs,
        }

        try:
            return render(request, 'core/logs.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def favorites(request):
        try:
            favorites = Document.objects.filter(likes=request.user.id)
        except Document.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Document} not found."})

        for f in favorites:
            f.is_liked_by_user = True

        context = {
            # 'favorites': Document.objects.filter(is_liked_by_user=True),
            'favorites': favorites,
        }

        try:
            return render(request, 'core/favorites.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def my_tasks(request):
        template = 'core/my_tasks.html'
        try:
            all_objects = DocumentEditPurgatory.objects.all()
        except DocumentEditPurgatory.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{DocumentEditPurgatory} not found."})

        context = {
            'all_objects': all_objects,
        }

        try:
            return render(request, template, context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    def about(request):
        try:
            return render(request, 'core/about.html')
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.', })

    @staticmethod
    @SupportFunctions.allow_groups()
    def approve_revision(request, pk, slug):
        try:
            current_revision = DocumentEditPurgatory.objects.filter(pk=pk).get()
        except DocumentEditPurgatory.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{DocumentEditPurgatory} not found."})

        SupportFunctions.approve_and_upload_revision(current_revision)

        try:
            return redirect('my tasks')
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

    @staticmethod
    @SupportFunctions.allow_groups()
    def delete_revision(request, pk, slug):
        try:
            current_revision = DocumentEditPurgatory.objects.filter(pk=pk).get()
        except DocumentEditPurgatory.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{DocumentEditPurgatory} not found."})

        current_revision.delete()

        try:
            return redirect('my tasks')
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

# -------------------------------------------------------------------------------------

    @staticmethod
    @SupportFunctions.allow_groups()
    def requirements_matrix(request):
        choice_form = RequirementsDocumentForm()
        choice = None
        requirement_form = RequirementsForm()

        if 'button1' in request.POST:
            try:
                requirement_form = RequirementsForm(request.POST)
                if requirement_form.is_valid():
                    requirement_form.save()
                    requirement_form = RequirementsForm()
                    choice_form = RequirementsDocumentForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                requirement_form.add_error(None, "An error occurred during form processing.")
                choice_form = RequirementsDocumentForm()

        elif 'req_choice' in request.POST:
            try:
                choice_form = RequirementsDocumentForm(request.POST)
                if choice_form.is_valid():
                    choice = choice_form.cleaned_data['requirements_document_dropdown']
                requirement_form = RequirementsForm()
            except Exception as e:
                print(f"Form processing error: {e}")
                choice_form.add_error(None, "An error occurred during form processing.")
                requirement_form = RequirementsForm()

        else:   # GET
            requirement_form = RequirementsForm()
            choice_form = RequirementsDocumentForm()

        if choice is not None and choice != 'All':
            try:
                requirements = Requirements.objects.filter(external_document=choice)
            except Requirements.DoesNotExist:
                return render(request, 'error.html', {'error_message': f"{Requirements} not found."})
        else:
            try:
                requirements = Requirements.objects.all().order_by('organization', 'clause')
            except Requirements.DoesNotExist:
                return render(request, 'error.html', {'error_message': f"{Requirements} not found."})

        context = {
            'requirement_form': requirement_form,
            'choice_form': choice_form,
            'requirements': requirements,
        }

        try:
            return render(request, 'core/requirements_matrix.html', context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.', })

    @staticmethod
    @SupportFunctions.allow_groups()
    def show_requirement(request, pk, slug):
        template = 'core/show_requirement.html'

        try:
            current_requirement = Requirements.objects.filter(pk=pk).get()
        except Requirements.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Requirements} not found."})

        context = {
            'requirement': current_requirement,
        }

        try:
            return render(request, template, context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.', })

    @staticmethod
    @SupportFunctions.allow_groups()
    @SupportFunctions.log_entry(True)
    def edit_requirement(request, pk, slug):
        template = 'core/edit_requirement.html'

        try:
            current_requirement = Requirements.objects.filter(pk=pk).get()
        except Requirements.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Requirements} not found."})

        if request.method == 'GET':
            form = RequirementsEditForm(instance=current_requirement)
        else:
            form = RequirementsEditForm(request.POST, instance=current_requirement)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Edited a requirement `{output}`")

                try:
                    return redirect('requirements matrix')
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.', })

        context = {
            'form': form,
            'requirement': current_requirement,
        }

        try:
            return render(request, template, context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.', })

    @staticmethod
    @SupportFunctions.allow_groups()
    @SupportFunctions.log_entry(True)
    def delete_requirement(request, pk, slug):
        template = 'core/delete_requirement.html'

        try:
            current_requirement = Requirements.objects.filter(pk=pk).get()
        except Requirements.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{Requirements} not found."})

        if request.method == 'GET':
            form = RequirementsDeleteForm(instance=current_requirement)
        else:
            form = RequirementsDeleteForm(request.POST, instance=current_requirement)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Deleted a requirement `{output}`")

                try:
                    return redirect('requirements matrix')
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.', })

        context = {
            'form': form,
            'requirement': current_requirement,
        }

        try:
            return render(request, template, context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.', })
