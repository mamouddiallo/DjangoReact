from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from student.models import StudentModel
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import EmployeeModel
from .serializers import EmployeeSerializer
from django.http import Http404

# Create your views here.
@api_view(['GET', 'POST'])
def api_views(request):
    if request.method == "GET":
        students = StudentModel.objects.all()
        serialiser = StudentSerializer(students, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serialiser = StudentSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response (serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT","DELETE"])
def studentDetail_views(request, pk):
    try:
        student = StudentModel.objects.get(pk=pk)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serialiser = StudentSerializer(student)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serialiser = StudentSerializer(student, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_200_OK)
        else:
            return Response(serialiser.errors, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class Employees(APIView):
    def get(self, request):
        employees = EmployeeModel.objects.all()
        serialiser = EmployeeSerializer(employees, many=True)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serialiser = EmployeeSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmployeesDetail(APIView):
    def get_object(self, pk):
        try:
            return EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        employee = self.get_object(pk)
        serialiser = EmployeeSerializer(employee)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serialiser = EmployeeSerializer(employee, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_200_OK)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
        
        