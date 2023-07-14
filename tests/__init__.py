"""
erp_demo                            (django project)
    actionplan_mng                  (django app)
        views.py                    (.py file)
            def index(request):     (function)
            def create(request):    (function)
            def show(request):      (function)
        forms.py                    (.py file)
            class CreateForm:       (class)


tests                               (tests project)
    actionplan_mng                  (package)
        views                       (package)
            test_index.py           (.py file)      max 10-15 tests in a file
            test_create.py          (.py file)
            test_show.py            (.py file)
        forms                       (package)
            test_CreateForm.py     (.py file)


        or views.py                 (.py file)      if not much tests


We test models if they have validators

"""
