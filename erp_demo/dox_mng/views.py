from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.text import slugify

from erp_demo.main_app.custom_logic import SupportFunctions
from erp_demo.dox_mng.forms import DocumentForm, DocumentEditForm, \
    DocumentDeleteForm, DocumentTypeForm
from erp_demo.dox_mng.models import Document, DocumentEditPurgatory


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

        all_objects = SupportFunctions.extract_entry_by_choice(table, column_name, choice)

        context = {
            'all_objects': all_objects,
            'choice_form': form,
        }
        return render(request, template, context)

    # added for likes
    @staticmethod
    def like_document(request, pk):

        liked_document = Document.objects.get(id=pk)

        if liked_document.is_liked_by_user:
            liked_document.is_liked_by_user = False
            liked_document.save()
        else:
            liked_document.is_liked_by_user = True
            liked_document.save()

        redirect_path = request.META['HTTP_REFERER']
        return redirect(redirect_path)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def add_document(request):
        template = 'dox_mng/add_document.html'
        if request.method == 'GET':
            form = DocumentForm()
        else:
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                output = form.save()    # get the created object
                SupportFunctions.log_info(f"Added a document `{output.name}`")
                return redirect('document list')
        context = {
            'form': form,
        }
        return render(request, template, context)

    @staticmethod
    def show_document(request, pk, slug):
        template = 'dox_mng/show_document.html'
        current_document = Document.objects.filter(pk=pk).get()
        context = {
            'document': current_document,
        }
        return render(request, template, context)

    # @staticmethod
    # @SupportFunctions.log_entry(True)
    # def edit_document(request, pk, slug):
    #     template = 'dox_mng/edit_document.html'
    #     current_document = Document.objects.filter(pk=pk).get()
    #     if request.method == 'GET':
    #         form = DocumentEditForm(instance=current_document)
    #     else:
    #         form = DocumentEditForm(request.POST, request.FILES, instance=current_document)
    #         if form.is_valid():
    #             output = form.save()
    #             SupportFunctions.log_info(f"Edited a document `{output.name}`")
    #             return redirect('document list')
    #     context = {
    #         'form': form,
    #         'document': current_document,
    #     }
    #     return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def edit_document(request, pk, slug):
        template = 'dox_mng/edit_document.html'
        current_document = Document.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = DocumentEditForm(instance=current_document)
        else:
            form = DocumentEditForm(request.POST, request.FILES, instance=current_document)
            if form.is_valid():
                output = SupportFunctions.new_revision(form)
                SupportFunctions.log_info(f"Edited a document `{output}`")
                return redirect('document list')
        context = {
            'form': form,
            'document': current_document,
        }
        return render(request, template, context)

    @staticmethod
    @SupportFunctions.log_entry(True)
    def delete_document(request, pk, slug):
        template = 'dox_mng/delete_document.html'
        current_document = Document.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = DocumentDeleteForm(instance=current_document)
        else:
            form = DocumentDeleteForm(request.POST, instance=current_document)
            if form.is_valid():
                output = form.save()
                SupportFunctions.log_info(f"Deleted a document `{output.name}`")
                return redirect('document list')
        context = {
            'form': form,
            'document': current_document,
        }
        return render(request, template, context)
