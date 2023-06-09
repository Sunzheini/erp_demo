from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType

from erp_demo.custom_logic.custom_prototypes import PrototypeViews


# class ActionsMngViews(PrototypeViews):
#     def get_related_objects_view(self, request, content_type_id):
#         content_type = ContentType.objects.get_for_id(content_type_id)
#         model = content_type.model_class()
#         objects = model.objects.all()
#         return JsonResponse([{'id': obj.id, 'name': str(obj)} for obj in objects], safe=False)

class ActionsMngViews(PrototypeViews):
    def get_related_objects_view(self, request, content_type_id):
        content_type = ContentType.objects.get(id=content_type_id)
        model = content_type.model_class()
        objects = model.objects.all()
        return JsonResponse([{'id': obj.id, 'name': str(obj)} for obj in objects], safe=False)

