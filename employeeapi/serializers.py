from rest_framework import serializers

from employeeapi.models import EmployeeAPI

class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeAPI
        fields='__all__'