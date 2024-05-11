from rest_framework import serializers
from .models import Reg_Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Employee
        fields = ['name', 'email', 'age', 'gender']
