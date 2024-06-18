from django.urls import path
from erp_demo.family_tree.views import index


urlpatterns = [
    # http://localhost:8000/family-tree/index/
    path('index/', index, name='index'),
]
