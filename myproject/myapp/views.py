from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.

class EmployeeView(viewsets.ModelViewSet):  
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Employee
# from .serializers import EmployeeSerializer

# class EmployeeCrud(APIView):
#     def get(self, request):
#         # Retrieve all Person objects
#         persons = Employee.objects.all()
#         serializer = EmployeeSerializer(persons, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         # Create a new Person object
#         serializer = EmployeeSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request):
#         # Update an existing Person object
#         try:
#             person = Employee.objects.get(id=request.data['id'])
#         except Employee.DoesNotExist:
#             return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = EmployeeSerializer(person, data=request.data, partial=False)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request):
#         # Partially update an existing Person object
#         try:
#             person = Employee.objects.get(id=request.data['id'])
#         except Employee.DoesNotExist:
#             return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = EmployeeSerializer(person, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         # Delete a Person object
#         try:
#             person = Employee.objects.get(id=request.data['id'])
#         except Employee.DoesNotExist:
#             return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

#         person.delete()
#         return Response({"message": "Person deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    