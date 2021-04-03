from .models import Permission
from rest_framework import serializers


class ListPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['user', 'description', 'date_created', 'status']
        # fields = '__all__'


class PermissionDetail(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['user', 'description', 'date_created', 'status']

class CreatePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['user', 'description', 'status']

class UpdatePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['user', 'description', 'status']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
