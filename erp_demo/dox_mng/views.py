from django.shortcuts import render, redirect
from django.utils.text import slugify

from erp_demo.dox_mng.forms import DocumentForm, \
    DocumentEditForm, DocumentDeleteForm
from erp_demo.dox_mng.models import Document


def index(request):
    context = {}
    return render(request, 'index.html', context)


def document_list(request):

    # (re)creation of slugs
    all_documents = Document.objects.all()
    for document in all_documents:
        document.slug = slugify(document.name)
    Document.objects.bulk_update(all_documents, ['slug'])
    # ---

    context = {
        'all_documents': Document.objects.all(),
    }
    return render(request, 'document_list.html', context)


def add_document(request):
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
    return render(request, 'add_document.html', context)


def edit_document(request, pk, slug):
    current_document = Document.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = DocumentEditForm(instance=current_document)
    else:
        form = DocumentEditForm(request.POST, instance=current_document)
        if form.is_valid():
            form.save()
            return redirect('document list')
    context = {
        'form': form,
        'document': current_document,
    }
    return render(request, 'edit_document.html', context)


def delete_document(request, pk, slug):
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
    return render(request, 'delete_document.html', context)
