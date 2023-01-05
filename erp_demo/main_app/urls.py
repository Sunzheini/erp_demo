from django.urls import path, include

from erp_demo.main_app.views import index

urlpatterns = [
    path('', index, name='index'),
]
