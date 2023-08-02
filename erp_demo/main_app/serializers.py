from rest_framework import serializers

from erp_demo.hr_mng.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'position')
