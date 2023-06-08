from django.shortcuts import render


class OperationsAppViews:
    def __init__(self):
        self.context = {}

    def index(self, request):
        return render(request, 'operations_mng/operations_mng_index.html', self.context)
