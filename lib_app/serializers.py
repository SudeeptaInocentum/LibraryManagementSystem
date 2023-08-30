from rest_framework import serializers
from .models import *

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class GetDepartmentSerializer(serializers.ModelSerializer):
    building_id = BuildingSerializer(many=True)
    class Meta:
        model = Department
        fields = '__all__'

class GetListDepartmentSerializer(serializers.ModelSerializer):
    building_id = BuildingSerializer()

    class Meta:
        model = Department
        fields = '__all__'

class CreateSectionSerializer(serializers.ModelSerializer):
    department_id = GetDepartmentSerializer()
    class Meta:
        model = Section
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class CreateBooksSerializer(serializers.ModelSerializer):
    location = SectionSerializer()
    class Meta:
        model = Books
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CreateIssuenceSerializer(serializers.ModelSerializer):
    member_id = UserSerializer()
    Admin_id = AdminSerializer()
    issued_book_id = BooksSerializer()
    class Meta:
        model = Issuence
        fields = '__all__'

class IssuenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issuence
        fields = '__all__'
