from django.utils.text import slugify
from erp_demo.dox_mng.models import Document


class SupportFunctions:
    @staticmethod
    def recreation_of_slugs(some_model):
        all_objects = some_model.objects.all()

        for single_object in all_objects:
            if single_object.slug is None:
                single_object.slug = slugify(single_object.name)
        some_model.objects.bulk_update(all_objects, ['slug'])

    @staticmethod
    def extract_documents_by_type(selected_type):
        if selected_type == 'All':
            extracted_documents = Document.objects.all()
            return extracted_documents
        extracted_documents = Document.objects.filter(type=selected_type)
        return extracted_documents
