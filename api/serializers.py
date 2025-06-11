from rest_framework import serializers
from student.models import StudentModel
from employee.models import EmployeeModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"
        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = "__all__"