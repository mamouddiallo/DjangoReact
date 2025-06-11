from django.urls import path
from .import views
from student.views import student_views

urlpatterns = [
    path('students/',views.api_views, name="student_views" ),
    path('students/<int:pk>/', views.studentDetail_views, name="studentDetail_views"),
    path('employees/', views.Employees.as_view(), name="Employees"),
    path('employees/<int:pk>/', views.EmployeesDetail.as_view(), name="EmployeesDetail"),
]