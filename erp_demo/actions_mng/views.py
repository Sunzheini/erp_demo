from django.shortcuts import render


class ActionsMngViews:
    def __init__(self):
        self.context = {}

    def index(self, request):
        return render(request, 'actions_mng/actions_mng_index.html', self.context)
