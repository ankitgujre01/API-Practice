from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Student
from .models import Employee, Teacher, Cars, Criminal
from .serializers import StudentSerializer, EmployeeSerializer, TeacherSerializer, CarsSerializer, CriminalSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
# from .serializers import EmployeeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer    
    
class CarsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer   # serializer class name must be unique among classes in this class.
    
    
class CriminalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Criminal.objects.all()
    serializer_class = CriminalSerializer    