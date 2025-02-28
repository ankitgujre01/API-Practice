from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Student
from .models import Employee
from .serializers import StudentSerializer, EmployeeSerializer
# from .serializers import EmployeeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class EmployeeSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer