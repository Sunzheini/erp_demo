from erp_demo.dox_mng.models import Document
from erp_demo.hr_mng.models import Employee

from django.utils.text import slugify

from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


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
            'slug',
        ]

        workbook = load_workbook(current_file_path)
        worksheet = workbook[workbook.sheetnames[0]]
        for row in range(3, 5):                        # 1 is first row, not 0
            info_to_update[row] = {
                'first_name': None,
                'last_name': None,
                'identification': None,
                'position': None,
                'slug': None,
            }
            for col in range(1, 6):                     # 1 is first col, not 0
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
    def sort_process_steps(process_obj, process_step_obj):
        p_list = []
        for process in range(len(process_obj.objects.all())):
            p_list.append([])

            for process_step in process_step_obj.objects.all():
                if process_step.parent_process.id == process_obj.objects.all()[process].id:
                    p_list[process].append(process_step)
        return p_list
