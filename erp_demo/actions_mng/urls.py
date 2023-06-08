from django.urls import path, include

from erp_demo.actions_mng.views import ActionsMngViews

urlpatterns = [
    path('', ActionsMngViews()
         .index, name='actions_mng_index'),
]
