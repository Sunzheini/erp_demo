from django.shortcuts import render, redirect

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.dox_mng.forms import DocumentForm, DocumentEditForm, \
    DocumentDeleteForm, DocumentTypeForm
from erp_demo.dox_mng.models import Document


class DoxMngViews:
    @staticmethod
    def dox_mng_index(request):
        context = {}
        return render(request, 'dox_mng/dox_mng_index.html', context)

    @staticmethod
    def document_list(request):     # ToDo: cache
        template = 'dox_mng/document_list.html'

        table = Document
        column_name = 'type'
        choice = None

        if request.method == 'GET':
            form = DocumentTypeForm()
        else:
            form = DocumentTypeForm(request.POST)
            if form.is_valid():
                choice = form.cleaned_data['document_type_dropdown']

        context = {
            'all_objects': SupportFunctions.extract_entry_by_choice(table, column_name, choice),
            'choice_form': form,
        }
        return render(request, template, context)

    @staticmethod
    def add_document(request):
        template = 'dox_mng/add_document.html'
        if request.method == 'GET':
            form = DocumentForm()
        else:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('document list')
        context = {
            'form': form,
        }
        return render(request, template, context)

    @staticmethod
    def edit_document(request, pk, slug):
        template = 'dox_mng/edit_document.html'
        current_document = Document.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = DocumentEditForm(instance=current_document)
        else:
            form = DocumentEditForm(request.POST, request.FILES, instance=current_document)
            if form.is_valid():
                form.save()
                return redirect('document list')
        context = {
            'form': form,
            'document': current_document,
        }
        return render(request, template, context)

    @staticmethod
    def delete_document(request, pk, slug):
        template = 'dox_mng/delete_document.html'
        current_document = Document.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = DocumentDeleteForm(instance=current_document)
        else:
            form = DocumentDeleteForm(request.POST, instance=current_document)
            if form.is_valid():
                form.save()
                return redirect('document list')
        context = {
            'form': form,
            'document': current_document,
        }
        return render(request, template, context)
