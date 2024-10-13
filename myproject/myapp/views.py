from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.

class EmployeeCrud(viewsets.ModelViewSet):  
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer