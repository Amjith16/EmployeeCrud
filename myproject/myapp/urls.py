
from django.urls import path
from . import views
from .views import EmployeeCrud



urlpatterns = [
    path("employee/", EmployeeCrud.as_view({'get': 'list',
        'post': 'create',
        'put': 'update',    
        'patch': 'partial_update',  
        'delete': 'destroy'}), name = "Employee"),
]