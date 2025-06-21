from django.urls import path, include
from .import views
from .views import EmployeeViewset, BlogsView, CommentsView, CommentsDetailView, BlogsDetailView
from student.views import student_views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'employees', views.EmployeeViewset, basename="employees")




urlpatterns = [
    path('students/',views.api_views, name="student_views" ),
    path('students/<int:pk>/', views.studentDetail_views, name="studentDetail_views"),
    # path('employees/', views.Employees.as_view(), name="Employees"),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name="EmployeesDetail"),
    path ('', include(router.urls)),
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    
    path('blogs/<int:pk>/', views.BlogsDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentsDetailView.as_view()),
]