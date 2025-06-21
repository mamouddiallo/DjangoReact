from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from api.paginations import CustomPagination
from blog.serializers import BlogSerializer, CommentSerializer
from student.models import StudentModel
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from employee.models import EmployeeModel
from .serializers import EmployeeSerializer
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from blog.models import BlogModel, CommentModel
from employee.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter


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
    
    
# class Employees(APIView):
#     def get(self, request):
#         employees = EmployeeModel.objects.all()
#         serialiser = EmployeeSerializer(employees, many=True)
#         return Response(serialiser.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serialiser = EmployeeSerializer(data=request.data)
#         if serialiser.is_valid():
#             serialiser.save()
#             return Response(serialiser.data, status=status.HTTP_200_OK)
#         return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class EmployeesDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return EmployeeModel.objects.get(pk=pk)
#         except EmployeeModel.DoesNotExist:
#             raise Http404
        
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serialiser = EmployeeSerializer(employee)
#         return Response(serialiser.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serialiser = EmployeeSerializer(employee, data=request.data)
#         if serialiser.is_valid():
#             serialiser.save()
#             return Response(serialiser.data, status=status.HTTP_200_OK)
#         return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)
        
"""
# Mixins      
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

# Mixins

class EmployeesDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    
    def get(self, request, pk):
        return self.update(request, pk)
    
"""

# Generics 

# class Employees(generics.ListAPIView):
#     queryset = EmployeeModel.objects.all()
#     serializer_class =  EmployeeSerializer
    

# # Génerics

# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EmployeeModel.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'

"""
class EmployeeViewset(viewsets.ViewSet): # type: ignore
    def list(self, request):
        queryset = EmployeeModel.objects.all()
        serialiser = EmployeeSerializer(queryset, many=True)
        return Response(serialiser.data)
    
    def create(self, request):
        serialiser = EmployeeSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk):
        employee = EmployeeModel.objects.get(pk=pk)
        serialiser = EmployeeSerializer(employee)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        employee = get_object_or_404(EmployeeModel, pk=pk)
        serialiser = EmployeeSerializer(employee, data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        
    def delete(self, request, pk):
        employee = get_object_or_404(EmployeeModel, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter

class BlogsView(generics.ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title', 'blog_body']
    ordering_fields = ['id', 'blog_title']
    
    

class CommentsView(generics.ListCreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    

class BlogsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    
