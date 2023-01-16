from django.urls import path, include

from erp_demo.main_app.views import MainAppViews


urlpatterns = [
    path('', MainAppViews().index, name='index'),
    path('manage_db/', MainAppViews().manage_db, name='manage db'),
    path('contact-list/', MainAppViews().contact_list, name='contact list'),
]
