import os

from django.shortcuts import render, redirect

from erp_demo.custom_logic.custom_logic import SupportFunctions, DataManipulation
from erp_demo.dox_mng.forms import DocumentEditForm, DocumentTypeForm
from erp_demo.dox_mng.models import Document
from erp_demo.custom_logic.custom_prototypes import PrototypeViews


class DoxMngViews(PrototypeViews):
    @SupportFunctions.login_check
    @SupportFunctions.log_entry(True)
    def create_view(self, request):
        self._empty_context()
        form = self._return_form_based_on_method(request, self.create_form)

        if request.method == 'GET':
            self._add_form_to_context(form)

            try:
                return render(request, self.create_template, self.context)
            except Exception as e:
                print(f"Unexpected error: {e}")
                return render(request, 'error.html',
                              {'error_message': f'An unexpected error occurred: {e}.'})

    # new logic for revisions
    # ---------------------------------------------------------------------------------------

        elif request.method == 'POST':
            if form.is_valid():
                output = SupportFunctions.new_revision(form)
                SupportFunctions.log_info(f"Created a document `{output.name}`")

        try:
            return redirect(self.redirect_url)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    # ---------------------------------------------------------------------------------------

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

        try:
            return render(request, self.list_template, self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    @SupportFunctions.login_check
    def show_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk, request)

        # use different iframe based on document extension
        # ---------------------------------------------------------------------------------------
        form = self.view_form(instance=current_object)
        file_extension = ''
        allowed_extensions = ['.doc', '.docx', '.xls', '.xlsx']

        if current_object.attachment:
            file_extension = os.path.splitext(current_object.attachment.url)[1].lower()
        if file_extension in allowed_extensions:
            self.context['is_file'] = True

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)

        try:
            return render(request, self.show_template, self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    # added for likes
    @staticmethod
    def like_document(request, pk):
        try:
            current_document = Document.objects.get(id=pk)
        except Document.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"Document not found."})

        if current_document.likes.filter(id=request.user.id).exists():
            current_document.likes.remove(request.user)
        else:
            current_document.likes.add(request.user)

        redirect_path = request.META['HTTP_REFERER']

        try:
            return redirect(redirect_path)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

    @SupportFunctions.login_check
    def edit_view(self, request, pk, slug):
        self._empty_context()
        current_object = self._main_object_single(pk, request)

        # new logic for revisions
        # ---------------------------------------------------------------------------------------
        if request.method == 'GET':
            form = DocumentEditForm(instance=current_object)
        else:
            form = DocumentEditForm(request.POST, request.FILES, instance=current_object)
            if form.is_valid():
                # output = form.save()      # before the logic for the new revisions
                output = SupportFunctions.new_revision(form)
                SupportFunctions.log_info(f"Edited a document `{current_object.name}`")

                try:
                    return redirect(self.redirect_url)
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    return render(request, 'error.html',
                                  {'error_message': f'An unexpected error occurred: {e}.'})

        # ---------------------------------------------------------------------------------------

        self._add_form_to_context(form)
        self._add_current_object_to_context(current_object)

        try:
            return render(request, self.edit_template, self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})
