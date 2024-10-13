
from django.urls import path, include
from . import views
from .views import EmployeeView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Employee', EmployeeView)



urlpatterns = [
    path("", include(router.urls)),
]