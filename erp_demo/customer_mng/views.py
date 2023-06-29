from erp_demo.custom_logic.custom_prototypes import PrototypeViews


# class CustomerAppViews(PrototypeViews):
#     pass


from django.shortcuts import render, redirect
from django.views import View
from erp_demo.customer_mng.models import Customer
from erp_demo.customer_mng.forms import CustomerForm, CustomerEditForm, CustomerDeleteForm, CustomerViewForm
from erp_demo.custom_logic.custom_logic import SupportFunctions


class BaseView(View):
    template_list = [
        'customer_mng/customer_mng_index.html',
        'customer_mng/customer_list.html',
        'customer_mng/add_customer.html',
        'customer_mng/show_customer.html',
        'customer_mng/edit_customer.html',
        'customer_mng/delete_customer.html',
    ]

    redirect_url = 'customer list'

    form_list = [
        # Create, View, Edit, Delete
        CustomerForm, CustomerViewForm, CustomerEditForm, CustomerDeleteForm,
    ]

    main_object = Customer
    are_files_used = True

    context = {}

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        return self.main_object.objects.filter(pk=pk).get()

    def _validate_and_log(self, form, action_done):
        if form.is_valid():
            output = form.save()
            SupportFunctions.log_info(f"{action_done} {self.main_object.__name__} `{output.name}`")


class IndexView(BaseView):
    def get(self, request, *args, **kwargs):
        self.context = {}
        return render(request, self.template_list[0], self.context)


class ListView(BaseView):
    def get(self, request, *args, **kwargs):
        self.context = {'all_objects': self.main_object.objects.all()}
        return render(request, self.template_list[1], self.context)


class CreateView(BaseView):
    def get(self, request, *args, **kwargs):
        self.context = {'form': self.form_list[0]()}
        return render(request, self.template_list[2], self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_list[0](request.POST, request.FILES if self.are_files_used else None)
        self._validate_and_log(form, 'Created')
        return redirect(self.redirect_url)


class ShowView(BaseView):
    def get(self, request, *args, **kwargs):
        current_object = self.get_object()
        form = self.form_list[1](instance=current_object)
        self.context = {'form': form, 'current_object': current_object}
        return render(request, self.template_list[3], self.context)


class EditView(BaseView):
    def get(self, request, *args, **kwargs):
        current_object = self.get_object()
        form = self.form_list[2](instance=current_object)
        self.context = {'form': form, 'current_object': current_object}
        return render(request, self.template_list[4], self.context)

    def post(self, request, *args, **kwargs):
        current_object = self.get_object()
        form = self.form_list[2](request.POST, request.FILES if self.are_files_used else None, instance=current_object)
        self._validate_and_log(form, 'Edited')
        return redirect(self.redirect_url)


class DeleteView(BaseView):
    def get(self, request, *args, **kwargs):
        current_object = self.get_object()
        form = self.form_list[3](instance=current_object)
        self.context = {'form': form, 'current_object': current_object}
        return render(request, self.template_list[5], self.context)

    def post(self, request, *args, **kwargs):
        current_object = self.get_object()
        form = self.form_list[3](request.POST, request.FILES if self.are_files_used else None, instance=current_object)
        if form.is_valid():
            current_object.delete()
            SupportFunctions.log_info(f"Deleted {self.main_object.__name__} `{current_object.name}`")
        return redirect(self.redirect_url)
