from django.utils.text import slugify
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

from erp_demo.dox_mng.models import Document
from erp_demo.hr_mng.models import Employee
from erp_demo.process_mng.models import ProcessStepToDocuments, \
    ProcessStep, Process


class SupportFunctions:
    @staticmethod
    def extract_documents_by_type(selected_type):
        if selected_type == 'All':
            extracted_documents = Document.objects.all()
            return extracted_documents
        extracted_documents = Document.objects.filter(type=selected_type)
        return extracted_documents

    @staticmethod
    def extract_employee_by_position(selected_position):
        if selected_position == 'All':
            extracted_employees = Employee.objects.all()
            return extracted_employees
        extracted_employees = Employee.objects.filter(position=selected_position)
        return extracted_employees

    # ToDo: hardcoded for file Demo.xlsx and Employee model
    @staticmethod
    def add_to_database(request_object):
        current_file_path = request_object['select_file']
        info_to_update = {
        }
        list_of_keys = [
            'first_name',
            'last_name',
            'identification',
            'position',
        ]

        workbook = load_workbook(current_file_path)
        worksheet = workbook[workbook.sheetnames[0]]
        for row in range(3, 5):                        # 1 is first row, not 0
            info_to_update[row] = {
                'first_name': None,
                'last_name': None,
                'identification': None,
                'position': None,
            }
            for col in range(1, 5):                     # 1 is first col, not 0
                char = get_column_letter(col)           # == chr(65 + col)
                info_to_update[row][list_of_keys[col-1]] = worksheet[char + str(row)].value

        Employee.objects.bulk_create([Employee(
            first_name=info_to_update[obj]['first_name'],
            last_name=info_to_update[obj]['last_name'],
            identification=info_to_update[obj]['identification'],
            position=info_to_update[obj]['position'],
            slug=slugify(f"{info_to_update[obj]['first_name']}-{info_to_update[obj]['last_name']}"),
        ) for obj in info_to_update.keys()])

        return 'Successfully added'

    @staticmethod
    def delete_database():
        Employee.objects.all().delete()
        ProcessStepToDocuments.objects.all().delete()
        ProcessStep.objects.all().delete()
        Process.objects.all().delete()
        Document.objects.all().delete()
        return 'Successfully deleted'

    @staticmethod
    def sort_process_steps(process_obj, process_step_obj):
        p_list = []
        for process in range(len(process_obj.objects.all())):
            p_list.append([])

            for process_step in process_step_obj.objects.all():
                if process_step.parent_process.id == process_obj.objects.all()[process].id:
                    p_list[process].append(process_step)
        return p_list

# ------------------------------------------------------------------------

    # ToDo: hardcoded for file Demo2.xlsx and All models
    @staticmethod
    def recreate_database(request_object):
        current_file_path = request_object['select_file']

        # Employee
        info_to_update = {
        }
        list_of_keys = [
            'first_name',
            'last_name',
            'identification',
            'position',
        ]

        workbook = load_workbook(current_file_path)
        worksheet = workbook[workbook.sheetnames[0]]
        for row in range(3, 5):                        # 1 is first row, not 0
            info_to_update[row] = {
                'first_name': None,
                'last_name': None,
                'identification': None,
                'position': None,
            }
            for col in range(1, 5):                     # 1 is first col, not 0
                char = get_column_letter(col)           # == chr(65 + col)
                info_to_update[row][list_of_keys[col-1]] = worksheet[char + str(row)].value

        Employee.objects.bulk_create([Employee(
            first_name=info_to_update[obj]['first_name'],
            last_name=info_to_update[obj]['last_name'],
            identification=info_to_update[obj]['identification'],
            position=info_to_update[obj]['position'],
            slug=slugify(f"{info_to_update[obj]['first_name']}-{info_to_update[obj]['last_name']}"),
        ) for obj in info_to_update.keys()])

        #  --------------------------------------------------

        # Document
        info_to_update = {
        }
        list_of_keys = [
            'type',
            'name',
            'revision',
            'owner',
        ]

        for row in range(8, 12):  # 1 is first row, not 0
            info_to_update[row] = {
                'type': None,
                'name': None,
                'revision': None,
                'owner': None,
            }
            for col in range(1, 5):  # 1 is first col, not 0
                char = get_column_letter(col)  # == chr(65 + col)
                info_to_update[row][list_of_keys[col - 1]] = worksheet[char + str(row)].value

        Document.objects.bulk_create([Document(
            type=info_to_update[obj]['type'],
            name=info_to_update[obj]['name'],
            revision=info_to_update[obj]['revision'],
            owner=info_to_update[obj]['owner'],
            slug=slugify(f"{info_to_update[obj]['name']}"),
        ) for obj in info_to_update.keys()])

        #  --------------------------------------------------

        # Process
        info_to_update = {
        }
        list_of_keys = [
            'type',
            'number',
            'name',
        ]

        for row in range(15, 17):  # 1 is first row, not 0
            info_to_update[row] = {
                'type': None,
                'number': None,
                'name': None,
            }
            for col in range(1, 4):  # 1 is first col, not 0
                char = get_column_letter(col)  # == chr(65 + col)
                info_to_update[row][list_of_keys[col - 1]] = worksheet[char + str(row)].value

        Process.objects.bulk_create([Process(
            type=info_to_update[obj]['type'],
            number=info_to_update[obj]['number'],
            name=info_to_update[obj]['name'],
        ) for obj in info_to_update.keys()])

        #  --------------------------------------------------

        # ProcessStep
        info_to_update = {
        }
        list_of_keys = [
            'type',
            'number',
            'name',
            'parent_process',
        ]

        for row in range(20, 22):  # 1 is first row, not 0
            info_to_update[row] = {
                'type': None,
                'number': None,
                'name': None,
                'parent_process': None,
            }
            for col in range(1, 4):  # 1 is first col, not 0
                char = get_column_letter(col)  # == chr(65 + col)
                info_to_update[row][list_of_keys[col - 1]] = worksheet[char + str(row)].value

        ProcessStep.objects.bulk_create([ProcessStep(
            type=info_to_update[obj]['type'],
            number=info_to_update[obj]['number'],
            name=info_to_update[obj]['name'],
            parent_process=Process.objects.all()[0]
        ) for obj in info_to_update.keys()])

        #  --------------------------------------------------

        return 'Successfully added \n' \
               '(*documents have no attachments and \n' \
               'process steps have no linked documents!)'
