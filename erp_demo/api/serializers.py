from rest_framework import serializers

from erp_demo.hr_mng.models import Employee, Positions


# python object to json, ModelSerializer is like ModelForm
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class ApiTestEmpSerializer(serializers.ModelSerializer):
    # on department not only show the id but all dep info
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = '__all__'

    # override create method to be able to create new employee (because of relation with department)
    def create(self, validated_data):
        position_code = validated_data.pop('position').get('code')
        try:
            position = Employee.objects.filter(name=position_code).get()
        except Employee.DoesNotExist:
            position = Employee.objects.create(name=position_code)
        return Employee.objects.create(position=position, **validated_data)
