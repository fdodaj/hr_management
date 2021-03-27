from rest_framework import serializers
from rest_framework.generics import DestroyAPIView
from rest_framework.serializers import ModelSerializer

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'role']


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_created', 'hire_date', 'role']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_created', 'hire_date', 'role']


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'role']


class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_deleted']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password']


class UpdatePasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password']
