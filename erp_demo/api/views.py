from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from erp_demo.api.models import ApiTestEmp, ApiTestDep
from erp_demo.api.serializers import ApiTestEmpSerializer, ApiTestDepSerializer, DemoSerializer


# class ApiTestEmpListView(ListAPIView):            # GET
class ApiTestEmpListView(ListCreateAPIView):        # GET, POST
    queryset = ApiTestEmp.objects.all()
    serializer_class = ApiTestEmpSerializer

    # implement to be able to filter by department_id
    def get_queryset(self):
        department_id = self.request.query_params.get('department_id')
        queryset = self.queryset
        if department_id:
            queryset = queryset.filter(department_id=department_id)
        return queryset.all()


class ApiTestDepListView(ListAPIView):
    queryset = ApiTestDep.objects.all()
    serializer_class = ApiTestDepSerializer


class DemoApiView(APIView):
    def get(self, request):
        employees = ApiTestEmp.objects.all()
        departments = ApiTestDep.objects.all()

        body = {
            'employees': employees,
            'departments': departments,

            'employees_count': ApiTestEmp.objects.count(),
            'first_department': ApiTestDep.objects.first().name,
            'department_names': departments,
        }

        serializer = DemoSerializer(body)
        return Response(serializer.data)


# view-sets
# -----------------------------------------------------------------------

class EmployeeViewSet(ModelViewSet):
    queryset = ApiTestEmp.objects.all()
    serializer_class = ApiTestEmpSerializer


# for frontend
# -----------------------------------------------------------------------

class IndexView(TemplateView):
    template_name = 'api/api_index.html'
