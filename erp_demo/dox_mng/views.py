from django.shortcuts import render, redirect

from erp_demo.custom_logic.custom_logic import SupportFunctions, DataManipulation
from erp_demo.dox_mng.forms import DocumentEditForm, DocumentTypeForm
from erp_demo.dox_mng.models import Document
from erp_demo.custom_logic.custom_prototypes import PrototypeViews


class DoxMngViews(PrototypeViews):
    @SupportFunctions.login_check
    def list_view(self, request):
        self._empty_context()

        # new logic for the dropdown
        # ---------------------------------------------------------------------------------------
        table = Document
        column_name = 'type'
        choice = None

        if request.method == 'GET':
            form = DocumentTypeForm()
        else:
            form = DocumentTypeForm(request.POST)
            if form.is_valid():
                choice = form.cleaned_data['document_type_dropdown']

        all_objects = DataManipulation.extract_entry_by_choice(request, table, column_name, choice)

        self.context['all_objects'] = all_objects
        self.context['choice_form'] = form
        # ---------------------------------------------------------------------------------------

        return render(request, self.list_template, self.context)

    # added for likes
    @staticmethod
    def like_document(request, pk):
        current_document = Document.objects.get(id=pk)

        if current_document.likes.filter(id=request.user.id).exists():
            current_document.likes.remove(request.user)
        else:
            current_document.likes.add(request.user)

        redirect_path = request.META['HTTP_REFERER']
        return redirect(redirect_path)

    @SupportFunctions.login_check
    def edit_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk)

        # new logic for the dropdown
        # ---------------------------------------------------------------------------------------
        if request.method == 'GET':
            form = DocumentEditForm(instance=current_object)
        else:
            form = DocumentEditForm(request.POST, request.FILES, instance=current_object)
            if form.is_valid():
                # output = form.save()      # before the logic for the new revisions
                output = SupportFunctions.new_revision(form)
                SupportFunctions.log_info(f"Edited a document `{current_object.name}`")

                return redirect(self.redirect_url)

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)
        return render(request, self.edit_template, self.context)
