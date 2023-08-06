from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView
from erp_demo.api.serializers import ApiTestEmpSerializer
from erp_demo.hr_mng.models import Employee


class ApiEmployeesView(ListCreateAPIView):        # GET, POST
    queryset = Employee.objects.all()
    serializer_class = ApiTestEmpSerializer

    # implement to be able to filter by position_id
    def get_queryset(self):
        position_id = self.request.query_params.get('position_id')
        queryset = self.queryset
        if position_id:
            queryset = queryset.filter(position_id=position_id)
        return queryset.all()


class IndexView(TemplateView):
    template_name = 'api/api_index.html'
