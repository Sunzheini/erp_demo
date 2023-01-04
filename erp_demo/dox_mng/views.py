from django.shortcuts import render, redirect

from erp_demo.dox_mng.custom_logicz import SupportFunctions
from erp_demo.dox_mng.forms import DocumentForm, DocumentEditForm, DocumentDeleteForm
from erp_demo.dox_mng.models import Document


def index(request):
    context = {}
    return render(request, 'index.html', context)


def document_list(request):
    template = 'document_list.html'

    SupportFunctions.recreation_of_slugs(Document)
    context = {'all_documents': Document.objects.all(), }
    return render(request, template, context)


def add_document(request):
    template = 'add_document.html'

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


def edit_document(request, pk, slug):
    template = 'edit_document.html'

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


def delete_document(request, pk, slug):
    template = 'delete_document.html'

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
