from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Student
from .models import Employee
from .serializers import StudentSerializer, EmployeeSerializer, TeacherSerializer
# from .serializers import EmployeeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeaTeachercher.objects.all()
    serializer_class = TeacherSerializer    