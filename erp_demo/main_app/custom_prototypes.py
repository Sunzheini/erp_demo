from django.shortcuts import render, redirect

from erp_demo.main_app.custom_logic import SupportFunctions


class PrototypeViews:
    def __init__(self, template_list, form_list, main_object, are_files_used: bool = False):
        self.index_template = template_list[0]
        self.list_template = template_list[1]
        self.create_template = template_list[2]
        self.show_template = template_list[3]
        self.edit_template = template_list[4]
        self.delete_template = template_list[5]

        self.create_form = form_list[0]
        self.edit_form = form_list[1]
        self.delete_form = form_list[2]

        self.main_object = main_object
        self.are_files_used = are_files_used

        self.context = {}

    def _main_object_queryset(self):
        return self.main_object.objects.all()

    def _main_object_single(self, pk):
        return self.main_object.objects.filter(pk=pk).get()

    def _empty_context(self):
        self.context = {}

    def _add_form_to_context(self, form):
        self.context['form'] = form

    def _add_current_object_to_context(self, current_object):
        self.context['current_object'] = current_object

    def _validate_and_log(self, form, action_done):
        if form.is_valid():
            output = form.save()
            SupportFunctions.log_info(f"{action_done} {self.main_object} `{output.name}`")
            return redirect(reversed(self.list_template))

    def _return_form_based_on_method(self, request, form_type, template_type, instance=None):
        if request.method == 'GET':
            if instance:
                form = form_type(instance=instance)
            else:
                form = form_type()
            self._add_form_to_context(form)
            return render(request, template_type, self.context)
        else:
            if request.method == 'POST' and not self.are_files_used:
                if instance:
                    form = form_type(request.POST, instance=instance)
                else:
                    form = form_type(request.POST)
                return form
            elif request.method == 'POST' and self.are_files_used:
                if instance:
                    form = form_type(request.POST, request.FILES, instance=instance)
                else:
                    form = form_type(request.POST, request.FILES)
                return form

    def index_view(self, request):
        self._empty_context()
        return render(request, self.index_template, self.context)

    def list_view(self, request):
        self._empty_context()
        self.context['all_objects'] = self._main_object_queryset()
        return render(request, self.list_template, self.context)

    def create_view(self, request):
        self._empty_context()
        form = self._return_form_based_on_method(request, self.create_form, self.create_template)
        self._validate_and_log(form, 'Created')

    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)
        form = self.edit_form(instance=current_object)

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.show_template, self.context)

    def edit_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)
        self._add_current_object_to_context(current_object)
        form = self._return_form_based_on_method(request, self.create_form, self.create_template, instance=current_object)
        self._validate_and_log(form, 'Edited')

    def delete_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)
        self._add_current_object_to_context(current_object)
        form = self._return_form_based_on_method(request, self.delete_form, self.delete_template, instance=current_object)
        self._validate_and_log(form, 'Deleted')

