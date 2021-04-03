from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from . import serializers

User = get_user_model()


def get_queryset(self):
    return User.objects.filter(is_deleted=False)


# Create user with authenicated password
class CreateUser(generics.CreateAPIView):
    queryset = get_queryset(serializers.UserSerializer)
    serializer_class = serializers.UserSerializer

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = Employee.objects.create(
            email=email,
            username=username,
            password=make_password(password))
        return user


# lsit all users that are not deleted
class ListUser(generics.ListAPIView):
    queryset = get_queryset(serializers.ListUserSerializer)
    serializer_class = serializers.ListUserSerializer


# get user with ID
class UserDetail(RetrieveAPIView):
    queryset = get_queryset(serializers.UserDetailSerializer)
    serializer_class = serializers.UserDetailSerializer


# update user by ID
class UpdateView(UpdateAPIView):
    queryset = get_queryset(serializers.UpdateUserSerializer)
    serializer_class = serializers.UpdateUserSerializer


# (soft)Delete an user
class UserDestroyAPIView(DestroyAPIView):
    queryset = get_queryset(serializers.UserSerializer)
    serializer_class = serializers.UserSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


# view user password
class UserPasswordView(RetrieveAPIView):
    queryset = get_queryset(serializers.UserPasswordSerializer)
    serializer_class = serializers.UserPasswordSerializer
