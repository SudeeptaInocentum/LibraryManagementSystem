import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Building, Department, Section, Books, Admin, User, Issuence
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class BuildingList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['name', 'address']
    def get(self, request):
        try:
            var = self.request.query_params.get('name')
            print(var)
            paginator = self.pagination_class()
            if var:
                buildings = Building.objects.filter(name=var)
            else:
                buildings = Building.objects.all()
            queryset = self.filter_queryset(buildings)
            page = paginator.paginate_queryset(queryset, request)
            serializer = BuildingSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = BuildingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BuildingDetails(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            building = Building.objects.get(id=id)
        except Building.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            building.delete()
            return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            building = Building.objects.get(id=id)
        except Building.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)

        try:
            serializer = BuildingSerializer(building, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            building = Building.objects.get(id=id)
            serializer = BuildingSerializer(building)
            return Response(serializer.data)
        except Building.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class DepartmentList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'code', 'floor', 'building_id__id']
    ordering_fields = ['name', 'code']
    def get(self, request):
        try:
            var = self.request.query_params.get('name')
            print(var)
            paginator = self.pagination_class()
            if var:
                department = Department.objects.filter(name=var).order_by("id")
            else:
                department = Department.objects.all().order_by("id")
            queryset = self.filter_queryset(department)
            page = paginator.paginate_queryset(queryset, request)
            serializer = GetListDepartmentSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = GetListDepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DepartmentDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            department.delete()
            return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            department = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)

        try:
            serializer = GetListDepartmentSerializer(department, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            department = Department.objects.get(id=id)
            serializer = GetListDepartmentSerializer(department)
            return Response(serializer.data)
        except Department.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class SectionList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'description']
    def get(self, request):
        try:
            var = self.request.query_params.get('name')
            print(var)
            paginator = self.pagination_class()
            if var:
                section = Section.objects.filter(name=var)
            else:
                section = Section.objects.all()
            queryset = self.filter_queryset(section)
            page = paginator.paginate_queryset(queryset, request)
            serializer = SectionSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SectionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SectionDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            section = Section.objects.get(id=id)
        except Section.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            section.delete()
            return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            section = Section.objects.get(id=id)
        except Section.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = SectionSerializer(section, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            section = Section.objects.get(id=id)
            serializer = SectionSerializer(section)
            return Response(serializer.data)
        except Section.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class BookList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'bar_code', 'writer']
    ordering_fields = ['name', 'description', 'bar_code', 'writer']
    def get(self, request):
        try:
            var = self.request.query_params.get('name')
            print(var)
            paginator = self.pagination_class()
            if var:
                book = Books.objects.filter(name=var)
            else:
                book = Books.objects.all()
            queryset = self.filter_queryset(book)
            page = paginator.paginate_queryset(queryset, request)
            serializer = BooksSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = BooksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            book = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            book.delete()
            return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            book = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = BooksSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            book = Books.objects.get(id=id)
            serializer = BooksSerializer(book)
            return Response(serializer.data)
        except Books.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class AdminList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'designation', 'phone_number']
    ordering_fields = ['name', 'designation', 'phone_number']
    def get(self, request):
        try:
            var = self.request.query_params.get('name')
            print(var)
            paginator = self.pagination_class()
            if var:
                _admin = Admin.objects.filter(name=var)
            else:
                _admin = Admin.objects.all()
            queryset = self.filter_queryset(_admin)
            page = paginator.paginate_queryset(queryset, request)
            serializer = AdminSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = AdminSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            admin = Admin.objects.get(id=id)
        except Admin.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            admin.delete()
            return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            admin = Admin.objects.get(id=id)
        except Admin.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = AdminSerializer(admin, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            admin = Admin.objects.get(id=id)
            serializer = AdminSerializer(admin)
            return Response(serializer.data)
        except Admin.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class UserList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address', 'email', 'joining_date']
    ordering_fields = ['name', 'address', 'email', 'joining_date']
    def get(self, request):
        try:
            var = self.request.query_params.get('name')
            print(var)
            paginator = self.pagination_class()
            if var:
                user = User.objects.filter(name=var)
            else:
                user = User.objects.all()
            queryset = self.filter_queryset(user)
            page = paginator.paginate_queryset(queryset, request)
            serializer = UserSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            user.delete()
            return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)


class IssuenceList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address', 'email', 'joining_date']
    ordering_fields = ['name', 'address', 'email', 'joining_date']
    def get(self, request):
        try:
            var = self.request.query_params.get('status')
            print(var)
            paginator = self.pagination_class()
            if var:
                issuence = Issuence.objects.filter(status=var)
            else:
                issuence = Issuence.objects.all()
            queryset = self.filter_queryset(issuence)
            page = paginator.paginate_queryset(queryset, request)
            serializer = IssuenceSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = IssuenceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class IssuenceDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        try:
            issuence = Issuence.objects.get(id=id)
        except Issuence.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            issuence.delete()
            return Response({"details": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            user = Issuence.objects.get(id=id)
        except Issuence.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = IssuenceSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            tb = traceback.format_exc()
            print(tb)
            error_message = str(ex)
            return Response({"Error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id):
        try:
            issuence = Issuence.objects.get(id=id)
            serializer = IssuenceSerializer(issuence)
            return Response(serializer.data)
        except Issuence.DoesNotExist:
            return Response({"Details": "Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
