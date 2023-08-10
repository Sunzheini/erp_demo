import time
from functools import wraps

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from erp_demo.actionplan_mng.models import ActionPlan, ActionPlanStep
from erp_demo.calibration_mng.models import MeasuringEquipment
from erp_demo.characteristics_mng.models import Characteristic
from erp_demo.control_plan_mng.models import ProcessControlPlan, ProcessControlPlanStep
from erp_demo.customer_mng.models import Customer
from erp_demo.defect_cat_mng.models import DefectCatalogue
from erp_demo.dox_mng.models import Document, DocumentEditPurgatory
from erp_demo.hr_mng.models import Employee, Trainings
from erp_demo.custom_logic import custom_collections
from erp_demo.interaction_mng.models import Interaction
from erp_demo.kpi_mng.models import Kpi
from erp_demo.main_app.models import CaptainsLog, Requirements
from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.maintenance_mng.models import Machine
from erp_demo.newactions_mng.models import NewAction
from erp_demo.nonconformity_mng.models import Nonconformity
from erp_demo.opportunity_mng.models import Opportunity
from erp_demo.organization_mng.models import Organization
from erp_demo.process_mng.models import ProcessStep, Process
from erp_demo.resource_mng.models import Resource
from erp_demo.review_mng.models import ManagementReview
from erp_demo.risk_mng.models import Risk
from erp_demo.supplier_mng.models import Supplier


class DataManipulation:

    # For forms that select specific properties before showing the results
    # -----------------------------------------------------------------------
    @staticmethod
    def extract_entry_by_choice(request, table, column_name, choice):
        try:
            all_documents = table.objects.all()
        except table.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{table.__name__} not found."})

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

# currently used in sorting employees by position
    @staticmethod
    def data_after_choice_form(table, column_name, choice):
        if choice == 'All':

            try:
                extracted_data = table.objects.all()
            except table.DoesNotExist:
                return None

            return extracted_data
        data = {column_name: choice}
        extracted_data = table.objects.filter(**data)

        return extracted_data

# Sort process steps
# -----------------------------------------------------------------------

    @staticmethod
    def sort_process_steps(process_obj, process_step_obj, choice):
        p_list = []

        try:
            all_processes = process_obj.objects.all()
        except process_obj.DoesNotExist:
            return None

        if choice == 'All':
            for process in all_processes:
                try:
                    process_steps = process_step_obj.objects.filter(parent_process=process)
                    p_list.append(list(process_steps))
                except process_step_obj.DoesNotExist:
                    return None

        elif choice is not None:
            chosen_process = process_obj.objects.get(number=choice)
            process_steps = process_step_obj.objects.filter(parent_process=chosen_process)
            p_list.append(list(process_steps))

        return p_list

    # Get list of process steps for a process
# -----------------------------------------------------------------------

    @staticmethod
    def get_process_step_list(process, process_step_obj):
        process_step_list = []

        for process_step in process_step_obj.objects.all():
            try:
                if process_step.parent_process.id == process.id:
                    process_step_list.append(process_step)
            except AttributeError:
                print(f"AttributeError: {process_step} has no attribute 'parent_process'")

        return process_step_list

# Dict with all employees and their owned processes in a list
# -----------------------------------------------------------------------

    @staticmethod
    def get_owned_processes_list(employees, processes):
        try:
            all_employees = employees.objects.all()
        except employees.DoesNotExist:
            return None

        owned_processes_dict = {
            employee: [] for employee in all_employees
        }

        for process in processes.objects.all():
            try:
                if process.process_owner in owned_processes_dict.keys():
                    owned_processes_dict[process.process_owner].append(process)
            except AttributeError:
                print(f"AttributeError: {process} has no attribute 'process_owner'")

        return owned_processes_dict

    @staticmethod
    def get_owned_trainings_list(employees, trainings):

        try:
            all_employees = employees.objects.all()
        except employees.DoesNotExist:
            return None

        try:
            all_trainings = trainings.objects.all()
        except trainings.DoesNotExist:
            return None

        owned_trainings_dict = {
            employee: [] for employee in all_employees
        }

        for training in all_trainings:
            for employee in all_employees:
                try:
                    if training.id in employee.trainings.all().values_list('id', flat=True):
                        owned_trainings_dict[employee].append(training)
                except AttributeError:
                    print(f"AttributeError: {employee} has no attribute 'trainings'")

        return owned_trainings_dict

    # A list with all from interactions of a specific process
    # -----------------------------------------------------------------------
    @staticmethod
    def get_from_interactions_list(current_process):
        try:
            process_step_object_list = ProcessStep.objects.filter(parent_process=current_process)
        except ProcessStep.DoesNotExist:
            return None

        try:
            from_interactions = Interaction.objects.filter(to_process_step__in=process_step_object_list)
        except Interaction.DoesNotExist:
            return None

        return from_interactions

    @staticmethod
    def get_to_interactions_list(current_process):
        try:
            process_step_object_list = ProcessStep.objects.filter(parent_process=current_process)
        except ProcessStep.DoesNotExist:
            return None

        try:
            to_interactions = Interaction.objects.filter(from_process_step__in=process_step_object_list)
        except Interaction.DoesNotExist:
            return None

        return to_interactions

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
                            operation=f"{custom_collections.logging_info_stack.pop()}",
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
        try:
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
                slug=slugify(f"{translate_to_maimunica(the_form.cleaned_data['name'])}"),
            )
        except Exception as e:
            print(f"Unexpected error: {e}")
            result = None

        return result

    @staticmethod
    def approve_and_upload_revision(prototype: DocumentEditPurgatory):
        try:
            document_to_delete = Document.objects.filter(name=prototype.name)
        except Document.DoesNotExist:
            document_to_delete = None
            print(f"Document {prototype.name} does not exist.")

        if document_to_delete.exists():
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

        else:
            try:
                Document.objects.create(
                    type=prototype.type,
                    number=prototype.number,
                    name=prototype.name,
                    revision=1,
                    creation_date=prototype.creation_date,
                    revision_date=prototype.revision_date,
                    revision_details=prototype.revision_details,
                    status=prototype.status,
                    owner=prototype.owner,
                    attachment=prototype.attachment,
                    slug=slugify(f"{translate_to_maimunica(prototype.name)}"),
                )
                prototype.delete()
            except Exception as e:
                print(f"Unexpected error: {e}")

    # search results on the index page
    # -----------------------------------------------------------------------
    @staticmethod
    def search_results(search_pattern, choice):
        result = {}

        if choice == 'All':
            try:
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
                interactions = Interaction.objects.filter(name__icontains=search_pattern)
                risks = Risk.objects.filter(name__icontains=search_pattern)
                opportunities = Opportunity.objects.filter(name__icontains=search_pattern)
                kpis = Kpi.objects.filter(name__icontains=search_pattern)
                resources = Resource.objects.filter(name__icontains=search_pattern)
                requirements = Requirements.objects.filter(description__icontains=search_pattern)
                nonconformities = Nonconformity.objects.filter(name__icontains=search_pattern)
                actions = NewAction.objects.filter(name__icontains=search_pattern)
                action_plans = ActionPlan.objects.filter(name__icontains=search_pattern)
                action_plan_steps = ActionPlanStep.objects.filter(name__icontains=search_pattern)
                suppliers = Supplier.objects.filter(name__icontains=search_pattern)
                measuring_equipments = MeasuringEquipment.objects.filter(name__icontains=search_pattern)
                machines = Machine.objects.filter(name__icontains=search_pattern)
                characteristics = Characteristic.objects.filter(name__icontains=search_pattern)
                control_plans = ProcessControlPlan.objects.filter(name__icontains=search_pattern)
                control_plan_steps = ProcessControlPlanStep.objects.filter(name__icontains=search_pattern)
                defect_catalogues = DefectCatalogue.objects.filter(name__icontains=search_pattern)
                management_reviews = ManagementReview.objects.filter(name__icontains=search_pattern)
            except Exception as e:
                print(f"Unexpected error: {e}")
                return None

            result['processes'] = processes
            result['process_steps'] = process_steps
            result['documents'] = documents
            result['employees'] = employee_set
            result['trainings'] = trainings
            result['organizations'] = organizations
            result['customers'] = customers
            result['interactions'] = interactions
            result['risks'] = risks
            result['opportunities'] = opportunities
            result['kpis'] = kpis
            result['resources'] = resources
            result['requirements'] = requirements
            result['nonconformities'] = nonconformities
            result['actions'] = actions
            result['action_plans'] = action_plans
            result['action_plan_steps'] = action_plan_steps
            result['suppliers'] = suppliers
            result['measuring_equipments'] = measuring_equipments
            result['machines'] = machines
            result['characteristics'] = characteristics
            result['control_plans'] = control_plans
            result['control_plan_steps'] = control_plan_steps
            result['defect_catalogues'] = defect_catalogues
            result['management_reviews'] = management_reviews

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

        elif choice == 'Interaction':
            interactions = Interaction.objects.filter(name__icontains=search_pattern)
            result['interactions'] = interactions

        elif choice == 'Risk':
            risks = Risk.objects.filter(name__icontains=search_pattern)
            result['risks'] = risks

        elif choice == 'Opportunity':
            opportunities = Opportunity.objects.filter(name__icontains=search_pattern)
            result['opportunities'] = opportunities

        elif choice == 'Kpi':
            kpis = Kpi.objects.filter(name__icontains=search_pattern)
            result['kpis'] = kpis

        elif choice == 'Resource':
            resources = Resource.objects.filter(name__icontains=search_pattern)
            result['resources'] = resources

        elif choice == 'Requirements':
            requirements = Requirements.objects.filter(description__icontains=search_pattern)
            result['requirements'] = requirements

        elif choice == 'Nonconformity':
            nonconformities = Nonconformity.objects.filter(name__icontains=search_pattern)
            result['nonconformities'] = nonconformities

        elif choice == 'NewAction':
            actions = NewAction.objects.filter(name__icontains=search_pattern)
            result['actions'] = actions

        elif choice == 'ActionPlan':
            action_plans = ActionPlan.objects.filter(name__icontains=search_pattern)
            result['action_plans'] = action_plans

        elif choice == 'ActionPlanStep':
            action_plan_steps = ActionPlanStep.objects.filter(name__icontains=search_pattern)
            result['action_plan_steps'] = action_plan_steps

        elif choice == 'Supplier':
            suppliers = Supplier.objects.filter(name__icontains=search_pattern)
            result['suppliers'] = suppliers

        elif choice == 'MeasuringEquipment':
            measuring_equipments = MeasuringEquipment.objects.filter(name__icontains=search_pattern)
            result['measuring_equipments'] = measuring_equipments

        elif choice == 'Machine':
            machines = Machine.objects.filter(name__icontains=search_pattern)
            result['machines'] = machines

        elif choice == 'Characteristic':
            characteristics = Characteristic.objects.filter(name__icontains=search_pattern)
            result['characteristics'] = characteristics

        elif choice == 'ProcessControlPlan':
            control_plans = ProcessControlPlan.objects.filter(name__icontains=search_pattern)
            result['control_plans'] = control_plans

        elif choice == 'ProcessControlPlanStep':
            control_plan_steps = ProcessControlPlanStep.objects.filter(name__icontains=search_pattern)
            result['control_plan_steps'] = control_plan_steps

        elif choice == 'DefectCatalogue':
            defect_catalogues = DefectCatalogue.objects.filter(name__icontains=search_pattern)
            result['defect_catalogues'] = defect_catalogues

        elif choice == 'ManagementReview':
            management_reviews = ManagementReview.objects.filter(name__icontains=search_pattern)
            result['management_reviews'] = management_reviews

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
            print(f"------------------ {exec_time:.3f} s ------------------")
            return result

        return wrapper
