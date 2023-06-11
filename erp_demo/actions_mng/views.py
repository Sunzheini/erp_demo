from django.shortcuts import render, redirect, get_object_or_404

from erp_demo.actions_mng.forms import ActionFormRisk, ActionFormTask, ActionFormOpportunity, ActionFormNonconformity, \
    ActionEditFormRisk, ActionEditFormTask, ActionEditFormOpportunity, ActionEditFormNonconformity, \
    ActionTypeForm
from erp_demo.actions_mng.models import Action
from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.nonconformity_mng.models import Nonconformity
from erp_demo.opportunity_mng.models import Opportunity
from erp_demo.risk_mng.models import Risk


class ActionsMngViews(PrototypeViews):
    def create_view_risk(self, request):
        template = 'actions_mng/add_action_risk.html'
        form_template = ActionFormRisk

        if request.method == 'POST':
            form = form_template(request.POST)
            if form.is_valid():
                form.save()
                return redirect('actions list')
        else:
            form = form_template()

        context = {'form': form}
        return render(request, template, context)

    def create_view_opportunity(self, request):
        template = 'actions_mng/add_action_opportunity.html'
        form_template = ActionFormOpportunity

        if request.method == 'POST':
            form = form_template(request.POST)
            if form.is_valid():
                form.save()
                return redirect('actions list')
        else:
            form = form_template()

        context = {'form': form}
        return render(request, template, context)

    def create_view_nonconformity(self, request):
        template = 'actions_mng/add_action_nonconformity.html'
        form_template = ActionFormNonconformity

        if request.method == 'POST':
            form = form_template(request.POST)
            if form.is_valid():
                form.save()
                return redirect('actions list')
        else:
            form = form_template()

        context = {'form': form}
        return render(request, template, context)

    def create_view_task(self, request):
        template = 'actions_mng/add_action_task.html'
        form_template = ActionFormTask

        if request.method == 'POST':
            form = form_template(request.POST)
            if form.is_valid():
                form.save()
                return redirect('actions list')
        else:
            form = form_template()

        context = {'form': form}
        return render(request, template, context)

    def distribute_show_links(self, request, pk, slug):
        try:
            obj = Risk.objects.get(pk=pk, slug=slug)
            return redirect('show risk', pk=pk, slug=slug)
        except Risk.DoesNotExist:
            pass

        try:
            obj = Opportunity.objects.get(pk=pk, slug=slug)
            return redirect('show opportunity', pk=pk, slug=slug)
        except Opportunity.DoesNotExist:
            pass

        try:
            obj = Nonconformity.objects.get(pk=pk, slug=slug)
            return redirect('show nonconformity', pk=pk, slug=slug)
        except Nonconformity.DoesNotExist:
            pass

        return redirect('actions list')

    def edit_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

        form = None
        print(current_object.type)
        if current_object.type == 'Task':
            form = self._return_form_based_on_method(request, ActionEditFormTask, instance=current_object)
        elif current_object.content_type.model == 'risk':
            form = self._return_form_based_on_method(request, ActionEditFormRisk, instance=current_object)
        elif current_object.content_type.model == 'opportunity':
            form = self._return_form_based_on_method(request, ActionEditFormOpportunity, instance=current_object)
        elif current_object.content_type.model == 'nonconformity':
            form = self._return_form_based_on_method(request, ActionEditFormNonconformity, instance=current_object)

        if request.method == 'GET':
            self._add_form_to_context(form)
            self._add_current_object_to_context(current_object)
            return render(request, self.edit_template, self.context)
        elif request.method == 'POST':
            self._add_form_to_context(form)
            self._add_current_object_to_context(current_object)
            self._validate_and_log(form, 'Edited')
            return redirect(self.redirect_url)

    def list_view(self, request):
        choice_form = ActionTypeForm
        choice = None

        if request.method == 'POST' and 'action_choice' in request.POST:
            choice_form = ActionTypeForm(request.POST)
            if choice_form.is_valid():
                choice = choice_form.cleaned_data['action_type_dropdown']
            choice_form = ActionTypeForm()
        else:
            choice_form = ActionTypeForm()

        if choice is not None and choice != 'All':
            all_objects = Action.objects.filter(type=choice)
        else:
            all_objects = Action.objects.all().order_by('id')

        context = {
            'choice_form': choice_form,
            'all_objects': all_objects,
        }

        return render(request, self.list_template, context)
