import time
from functools import wraps

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.text import slugify

from erp_demo.customer_mng.models import Customer
from erp_demo.dox_mng.models import Document, DocumentEditPurgatory
from erp_demo.hr_mng.models import Employee, Trainings
from erp_demo.custom_logic import custom_collections
from erp_demo.main_app.models import CaptainsLog
from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.organization_mng.models import Organization
from erp_demo.process_mng.models import ProcessStep, Process


class DataManipulation:

    # For forms that select specific properties before showing the results
    # -----------------------------------------------------------------------
    @staticmethod
    def extract_entry_by_choice(request, table, column_name, choice):
        # if choice == 'All':
        #     extracted_documents = table.objects.all()
        #     return extracted_documents
        # data = {column_name: choice}
        # extracted_documents = table.objects.filter(**data)
        #
        # return extracted_documents

        all_documents = table.objects.all()

        for ed in all_documents:
            ed.is_liked_by_user = False
            if ed.likes.filter(id=request.user.id).exists():
                ed.is_liked_by_user = True

        if choice == 'All':
            extracted_documents = all_documents
            return extracted_documents

        data = {column_name: choice}
        extracted_documents = table.objects.filter(**data)
        return extracted_documents

    @staticmethod
    def data_after_choice_form(table, column_name, choice):
        if choice == 'All':
            extracted_data = table.objects.all()
            return extracted_data
        data = {column_name: choice}
        extracted_data = table.objects.filter(**data)

        return extracted_data

# Sort process steps
# -----------------------------------------------------------------------

# original
    # @staticmethod
    # def sort_process_steps(process_obj, process_step_obj, choice):
    #     p_list = []
    #     all_processes = process_obj.objects.all()
    #     process_obj_length = len(all_processes)
    #
    #     if choice is None:
    #         pass
    #
    #     elif choice == 'All':
    #         for process in range(process_obj_length):
    #             p_list.append([])
    #
    #             for process_step in process_step_obj.objects.all():
    #                 if process_step.parent_process.id == all_processes[process].id:
    #                     p_list[process].append(process_step)
    #
    #     elif choice != 'All':
    #         chosen_process = process_obj.objects.filter(number=choice).get()
    #         p_list.append([])
    #
    #         for process_step in process_step_obj.objects.all():
    #             if process_step.parent_process.number == chosen_process.number:
    #                 p_list[0].append(process_step)
    #
    #     return p_list

# optimized
    @staticmethod
    def sort_process_steps(process_obj, process_step_obj, choice):
        p_list = []
        all_processes = process_obj.objects.all()

        if choice == 'All':
            for process in all_processes:
                process_steps = process_step_obj.objects.filter(parent_process=process)
                p_list.append(list(process_steps))
        elif choice is not None:
            chosen_process = process_obj.objects.get(number=choice)
            process_steps = process_step_obj.objects.filter(parent_process=chosen_process)
            p_list.append(list(process_steps))

        return p_list

# optimized with caching
#     @staticmethod
    # def sort_process_steps(process_obj, process_step_obj, choice):
    #     cache_key = f'sort_process_steps_{choice}'
    #     cache_version = cache.get(f'{cache_key}_version', 0)
    #
    #     cached_data = cache.get(cache_key)
    #
    #     if cached_data is not None and cache.get(f'{cache_key}_version', 0) == cache_version:
    #         # Use the cached data if it is up-to-date
    #
    #         return cached_data
    #
    #     p_list = []
    #     all_processes = process_obj.objects.all()
    #
    #     if choice == 'All':
    #         for process in all_processes:
    #             process_steps = process_step_obj.objects.filter(parent_process=process)
    #             p_list.append(list(process_steps))
    #     elif choice is not None:
    #         chosen_process = process_obj.objects.get(number=choice)
    #         process_steps = process_step_obj.objects.filter(parent_process=chosen_process)
    #         p_list.append(list(process_steps))
    #
    #     # Cache the processed data with the new version
    #     cache.set(cache_key, p_list)
    #     cache.set(f'{cache_key}_version', cache_version + 1)
    #
    #     return p_list

    # Get list of process steps for a process
# -----------------------------------------------------------------------

    @staticmethod
    def get_process_step_list(process, process_step_obj):
        process_step_list = []

        for process_step in process_step_obj.objects.all():
            if process_step.parent_process.id == process.id:
                process_step_list.append(process_step)

        return process_step_list

# Dict with all employees and their owned processes in a list
# -----------------------------------------------------------------------

    @staticmethod
    def get_owned_processes_list(employees, processes):
        owned_processes_dict = {
            employee: [] for employee in employees.objects.all()
        }

        for process in processes.objects.all():
            if process.process_owner in owned_processes_dict.keys():
                owned_processes_dict[process.process_owner].append(process)

        print(owned_processes_dict)
        return owned_processes_dict


class SupportFunctions:

    # Decorator + function: time measurement and writing to a log
    # -----------------------------------------------------------------------

    @staticmethod
    def log_entry(command):
        def decorator_depending_on_command(some_function):
            @wraps(some_function)
            def wrapper(*args, **kwargs):
                if command:
                    start = time.time()
                    result = some_function(*args, **kwargs)  # the function
                    end = time.time()
                    measurement = end - start

                    if custom_collections.logging_info_stack:
                        CaptainsLog.objects.create(
                            # operation=f"{custom_collections.logging_info_stack.pop()} "
                            #           f"with `{some_function.__name__}`",
                            operation=f"{custom_collections.logging_info_stack.pop()}",
                            # performed_at_time=end, # auto added in model
                            execution_time=f"{measurement:.5f} s",
                        )
                else:
                    result = some_function(*args, **kwargs)  # the function
                return result  # the function
            return wrapper
        return decorator_depending_on_command

    @staticmethod
    def log_info(function_result):
        custom_collections.logging_info_stack.append(function_result)

    # new document revision
    # -----------------------------------------------------------------------
    @staticmethod
    def new_revision(the_form):
        result = DocumentEditPurgatory.objects.create(
            type=the_form.cleaned_data['type'],
            number=the_form.cleaned_data['number'],
            name=the_form.cleaned_data['name'],
            revision=the_form.cleaned_data['revision'] + 1,
            creation_date=the_form.cleaned_data['creation_date'],
            revision_date=the_form.cleaned_data['revision_date'],
            revision_details=the_form.cleaned_data['revision_details'],
            # status=the_form.cleaned_data['status'],   # commented since i added to the form exclusion list
            status='Latest rev',
            owner=the_form.cleaned_data['owner'],
            attachment=the_form.cleaned_data['attachment'],
            # slug=slugify(f"{info_to_update[obj]['name']}"),
            # slug=slugify(f"{the_form.cleaned_data['owner']}-"
            #              f"{the_form.cleaned_data['type']}-"
            #              f"{the_form.cleaned_data['revision']}"),
            slug=slugify(f"{translate_to_maimunica(the_form.cleaned_data['name'])}"),
        )

        return result

    @staticmethod
    def approve_and_upload_revision(prototype: DocumentEditPurgatory):
        # document_to_delete = Document.objects.filter(name=prototype.name)
        # document_to_delete.delete()
        #
        # Document.objects.create(
        #     type=prototype.type,
        #     number=prototype.number,
        #     name=prototype.name,
        #     revision=prototype.revision,
        #     creation_date=prototype.creation_date,
        #     revision_date=prototype.revision_date,
        #     revision_details=prototype.revision_details,
        #     status=prototype.status,
        #     owner=prototype.owner,
        #     attachment=prototype.attachment,
        #     slug=slugify(f"{translate_to_maimunica(prototype.name)}"),
        # )
        # prototype.delete()

        document_to_delete = Document.objects.filter(name=prototype.name)

        document_to_delete.update(
            type=prototype.type,
            number=prototype.number,
            name=prototype.name,
            revision=prototype.revision,
            creation_date=prototype.creation_date,
            revision_date=prototype.revision_date,
            revision_details=prototype.revision_details,
            status=prototype.status,
            owner=prototype.owner,
            attachment=prototype.attachment,
            slug=slugify(f"{translate_to_maimunica(prototype.name)}"),
        )
        prototype.delete()

    # search results on the index page
    # -----------------------------------------------------------------------
    @staticmethod
    def search_results(search_pattern, choice):
        result = {}

        if choice == 'All':
            processes = Process.objects.filter(name__icontains=search_pattern)
            process_steps = ProcessStep.objects.filter(name__icontains=search_pattern)
            documents = Document.objects.filter(name__icontains=search_pattern)

            employees_by_first_names = list(Employee.objects.filter(first_name__icontains=search_pattern))
            employees_by_middle_names = list(Employee.objects.filter(middle_name__icontains=search_pattern))
            employees_by_last_names = list(Employee.objects.filter(last_name__icontains=search_pattern))
            employees_temp_list = employees_by_first_names + employees_by_middle_names + employees_by_last_names
            employee_set = set(employees_temp_list)

            trainings = Trainings.objects.filter(name__icontains=search_pattern)
            organizations = Organization.objects.filter(name__icontains=search_pattern)
            customers = Customer.objects.filter(name__icontains=search_pattern)

            result['processes'] = processes
            result['process_steps'] = process_steps
            result['documents'] = documents
            result['employees'] = employee_set
            result['trainings'] = trainings
            result['organizations'] = organizations
            result['customers'] = customers

        elif choice == 'Process':
            processes = Process.objects.filter(name__icontains=search_pattern)
            result['processes'] = processes

        elif choice == 'ProcessStep':
            process_steps = ProcessStep.objects.filter(name__icontains=search_pattern)
            result['process_steps'] = process_steps

        elif choice == 'Document':
            documents = Document.objects.filter(name__icontains=search_pattern)
            result['documents'] = documents

        elif choice == 'Employee':
            employees_by_first_names = list(Employee.objects.filter(first_name__icontains=search_pattern))
            employees_by_middle_names = list(Employee.objects.filter(middle_name__icontains=search_pattern))
            employees_by_last_names = list(Employee.objects.filter(last_name__icontains=search_pattern))
            employees_temp_list = employees_by_first_names + employees_by_middle_names + employees_by_last_names
            employee_set = set(employees_temp_list)

            result['employees'] = employee_set

        elif choice == 'Trainings':
            trainings = Trainings.objects.filter(name__icontains=search_pattern)
            result['trainings'] = trainings

        elif choice == 'Organization':
            organizations = Organization.objects.filter(name__icontains=search_pattern)
            result['organizations'] = organizations

        elif choice == 'Customer':
            customers = Customer.objects.filter(name__icontains=search_pattern)
            result['customers'] = customers

        return result

    # Decorator for allowing specific groups to access a page
    # -----------------------------------------------------------------------
    @staticmethod
    def allow_groups(groups=None):
        if groups is None:
            groups = []

        def decorator(view_func):
            def wrapper(request, *args, **kwargs):
                if not request.user.is_authenticated:
                    # return HttpResponse('Not authenticated!')
                    return redirect('login')

                if request.user.is_superuser or not groups:
                    return view_func(request, *args, **kwargs)

                user_groups = request.user.groups.filter(name__in=groups)

                if not user_groups:
                    return HttpResponse('Not in any of the allowed groups')

                return view_func(request, *args, **kwargs)

            return wrapper

        if callable(groups):
            func = groups
            groups = []
            return decorator(func)

        return decorator

    # updated
    @staticmethod
    def login_check(func):
        def wrapper(self, request, *args, **kwargs):
            if not self._check_if_logged_in(request):
                return redirect('login')
            else:
                return func(self, request, *args, **kwargs)

        return wrapper

    # Decorator to measure time for execution of a function
    # currently a middleware is used instead
    # -----------------------------------------------------------------------
    @staticmethod
    def measure_time(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            exec_time = end - start
            # print(f"Function {func.__name__} took {exec_time:.3f} s to execute")
            print(f"------------------ {exec_time:.3f} s ------------------")
            return result

        return wrapper