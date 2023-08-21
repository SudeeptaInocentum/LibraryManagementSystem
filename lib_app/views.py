from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Building, Department, Section, Books, Admin, User, Issuence
from .serializers import *


class BuildingList(APIView):
    def get(self, request):
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuildingDetails(APIView):
    def delete(self, request, id):
        try:
            building = Building.objects.get(id=id)
        except Building.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        building.delete()
        return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            building = Building.objects.get(id=id)
        except Building.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BuildingSerializer(building, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            building = Building.objects.get(id=id)
        except Building.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)

        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)
    

class DepartmentList(APIView):
    def get(self, request):
        department = Department.objects.all()
        serializer = CreateDepartmentSerializer(department, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateDepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetails(APIView):
    def delete(self, request, id):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        department.delete()
        return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CreateDepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            department = Department.objects.get(id=id)
            serializer = CreateDepartmentSerializer(department)
            return Response(serializer.data)
        except Department.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
    

class SectionList(APIView):
    def get(self, request):
        section = Section.objects.all()
        serializer = SectionSerializer(section, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SectionDetails(APIView):
    def delete(self, request, id):
        try:
            section = Section.objects.get(id=id)
        except Section.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        section.delete()
        return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            section = Section.objects.get(id=id)
        except Section.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            section = Section.objects.get(id=id)
            serializer = SectionSerializer(section)
            return Response(serializer.data)
        except Section.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class BookList(APIView):
    def get(self, request):
        book = Books.objects.all()
        serializer = BooksSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    def delete(self, request, id):
        try:
            book = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            book = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            book = Books.objects.get(id=id)
            serializer = BooksSerializer(book)
            return Response(serializer.data)
        except Books.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        

class AdminList(APIView):
    def get(self, request):
        _admin = Admin.objects.all()
        serializer = AdminSerializer(_admin, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDetails(APIView):
    def delete(self, request, id):
        try:
            admin = Admin.objects.get(id=id)
        except Admin.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        admin.delete()
        return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            admin = Admin.objects.get(id=id)
        except Admin.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            admin = Admin.objects.get(id=id)
            serializer = AdminSerializer(admin)
            return Response(serializer.data)
        except Admin.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        

class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class IssuenceList(APIView):
    def get(self, request):
        issuence = Issuence.objects.all()
        serializer = IssuenceSerializer(issuence, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IssuenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssuenceDetails(APIView):
    def delete(self, request, id):
        try:
            issuence = Issuence.objects.get(id=id)
        except Issuence.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        issuence.delete()
        return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        try:
            user = Issuence.objects.get(id=id)
        except Issuence.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = IssuenceSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            issuence = Issuence.objects.get(id=id)
            serializer = IssuenceSerializer(issuence)
            return Response(serializer.data)
        except Issuence.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)