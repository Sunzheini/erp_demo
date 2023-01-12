from erp_demo.dox_mng.models import Document
from erp_demo.hr_mng.models import Employee


class SupportFunctions:
    @staticmethod
    def extract_documents_by_type(selected_type):
        if selected_type == 'All':
            extracted_documents = Document.objects.all()
            return extracted_documents
        extracted_documents = Document.objects.filter(my_var=selected_type)
        return extracted_documents

    @staticmethod
    def extract_employee_by_position(selected_position):
        if selected_position == 'All':
            extracted_employees = Employee.objects.all()
            return extracted_employees
        extracted_employees = Employee.objects.filter(position=selected_position)
        return extracted_employees

    @staticmethod
    def sort_process_steps(obj1, obj2):
        result = obj2.objects.all()

# -----------------------------------------------------------------------------------
        # ToDo
        process_dict = {
            i.number: [] for i in obj1.objects.all()
        }
        print(process_dict)

        for j in obj2.objects.all():
            process_dict[j.parent_process.number].append(j.name)

        print(process_dict)

# -----------------------------------------------------------------------------------

        return result
