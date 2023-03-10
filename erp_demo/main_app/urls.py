from django.urls import path, include

from erp_demo.main_app.views import MainAppViews


urlpatterns = [
    path('', MainAppViews().index, name='index'),
    path('manage_db/', include([
        path('', MainAppViews().manage_db, name='manage db'),
        path('manage_db_all/', MainAppViews().manage_db_all, name='manage db all'),
    ])),
    # path('manage_db/', MainAppViews().manage_db, name='manage db'),
    path('organigramm/', MainAppViews().organigramm, name='organigramm'),
    path('logs/', MainAppViews().logs, name='logs'),
    path('favorites/', MainAppViews().favorites, name='favorites'),
    path('my-tasks/', MainAppViews().my_tasks, name='my tasks'),
    path('requirements-matrix/', MainAppViews().requirements_matrix, name='requirements matrix'),

    path('show-requirement/<int:pk>/<slug:slug>/', MainAppViews().show_requirement, name='show requirement'),
    path('edit-requirement/<int:pk>/<slug:slug>/', MainAppViews().edit_requirement, name='edit requirement'),
    path('delete-requirement/<int:pk>/<slug:slug>/', MainAppViews().delete_requirement, name='delete requirement'),
]
