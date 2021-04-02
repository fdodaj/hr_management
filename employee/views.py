from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from . import serializers

User = get_user_model()


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
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


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ListUserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(is_deleted=False)


class UpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UpdateUserSerializer


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = []
    queryset = User.objects.all()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


class UserPasswordView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserPasswordSerializer


class UpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UpdatePasswordSerializer


def get_queryset(self):
    return Employee.objects.filter(is_deleted=False)
