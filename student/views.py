from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_views(request):
    return HttpResponse("STUDENTS")