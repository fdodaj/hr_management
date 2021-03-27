from .models import Department
from rest_framework import serializers


class ListDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'users', 'department_leader', 'date_created']


class DepartmentDetail(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'users', 'department_leader', 'date_created']


class CreateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'users', 'department_leader']


class UpdateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'users', 'department_leader', ]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
