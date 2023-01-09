from erp_demo.dox_mng.models import Document


class SupportFunctions:

    @staticmethod
    def extract_documents_by_type(selected_type):
        if selected_type == 'All':
            extracted_documents = Document.objects.all()
            return extracted_documents
        extracted_documents = Document.objects.filter(type=selected_type)
        return extracted_documents
