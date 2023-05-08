from django.shortcuts import render, redirect

from erp_demo.main_app.custom_logic import SupportFunctions


class PrototypeViews:
    def __init__(self, template_list, redirect_url, form_list, main_object, are_files_used: bool = False):
        self.index_template = template_list[0]
        self.list_template = template_list[1]
        self.create_template = template_list[2]
        self.show_template = template_list[3]
        self.edit_template = template_list[4]
        self.delete_template = template_list[5]

        self.redirect_url = redirect_url

        self.create_form = form_list[0]
        self.view_form = form_list[1]
        self.edit_form = form_list[2]
        self.delete_form = form_list[3]

        self.main_object = main_object
        self.are_files_used = are_files_used

        self.context = {}

# Internal methods
# ---------------------------------------------------------------------------------------

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

    @SupportFunctions.log_entry(True)
    def _validate_and_log(self, form, action_done):
        if form.is_valid():
            output = form.save()
            SupportFunctions.log_info(f"{action_done} {self.main_object.__name__} `{output.name}`")

    def _return_form_based_on_method(self, request, form_type, instance=None):
        if request.method == 'GET':
            if instance:
                form = form_type(instance=instance)
            else:
                form = form_type()
            return form
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

    @staticmethod
    def _check_if_logged_in(request):
        return True if request.user.is_authenticated else False


# Views
# ---------------------------------------------------------------------------------------

    @SupportFunctions.login_check
    def index_view(self, request):
        self._empty_context()
        return render(request, self.index_template, self.context)

    @SupportFunctions.login_check
    def list_view(self, request):
        self._empty_context()

        # updated in some views
        # ---------------------------------------------------------------------------------------
        self.context['all_objects'] = self._main_object_queryset()
        # ---------------------------------------------------------------------------------------

        return render(request, self.list_template, self.context)

    @SupportFunctions.login_check
    def create_view(self, request):
        self._empty_context()
        form = self._return_form_based_on_method(request, self.create_form)

        if request.method == 'GET':
            self._add_form_to_context(form)
            return render(request, self.create_template, self.context)
        elif request.method == 'POST':
            self._validate_and_log(form, 'Created')
            return redirect(self.redirect_url)

    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

        # updated in some views
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)
        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.show_template, self.context)

    @SupportFunctions.login_check
    def edit_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)
        form = self._return_form_based_on_method(request, self.edit_form, instance=current_object)

        if request.method == 'GET':
            self._add_form_to_context(form)
            self._add_current_object_to_context(current_object)
            return render(request, self.edit_template, self.context)
        elif request.method == 'POST':
            self._add_form_to_context(form)
            self._add_current_object_to_context(current_object)
            self._validate_and_log(form, 'Edited')
            return redirect(self.redirect_url)

    @SupportFunctions.login_check
    def delete_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)
        form = self._return_form_based_on_method(request, self.delete_form, instance=current_object)

        if request.method == 'GET':
            self._add_form_to_context(form)
            self._add_current_object_to_context(current_object)
            return render(request, self.delete_template, self.context)
        elif request.method == 'POST':
            self._add_form_to_context(form)
            self._add_current_object_to_context(current_object)
            self._validate_and_log(form, 'Deleted')
            return redirect(self.redirect_url)
