from django.shortcuts import render


class NonconformityMngViews:
    def __init__(self):
        self.context = {}

    def index(self, request):
        return render(request, 'nonconformity_mng/nonconformity_mng_index.html', self.context)
