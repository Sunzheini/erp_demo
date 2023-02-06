from django.urls import path, include

from erp_demo.main_app.views import MainAppViews


urlpatterns = [
    path('', MainAppViews().index, name='index'),
    path('manage_db/', include([
        path('', MainAppViews().manage_db, name='manage db'),
        path('manage_db_all/', MainAppViews().manage_db_all, name='manage db all'),
    ])),
    # path('manage_db/', MainAppViews().manage_db, name='manage db'),
    path('contact-list/', MainAppViews().contact_list, name='contact list'),
    path('logs/', MainAppViews().logs, name='logs'),
    path('my-tasks/', MainAppViews().my_tasks, name='my tasks'),
]
