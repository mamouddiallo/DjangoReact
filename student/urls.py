from django.urls import path
from .import views

urlpatterns = [
    path('',views.student_views, name="student_views" ),
]