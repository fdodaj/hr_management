from .models import Permission
from rest_framework import serializers
from employee.models import Employee

class GetPto(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['pto']



class ListPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id','user', 'description', 'date_created', 'status']
        # fields = '__all__'


class PermissionDetail(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['user', 'description', 'date_created', 'status']

class CreatePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['user', 'description']

class UpdatePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['status']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
