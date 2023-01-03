from django.utils.text import slugify


class SupportFunctions:
    @staticmethod
    def recreation_of_slugs(some_model):
        all_objects = some_model.objects.all()

        for single_object in all_objects:
            if single_object.slug is None:
                single_object.slug = slugify(single_object.name)
        some_model.objects.bulk_update(all_objects, ['slug'])
