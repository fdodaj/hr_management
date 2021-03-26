from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView

from . import serializers
# from django.contrib.auth.models import User
from .models import User


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.CreateUserSerializer


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ListUserSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(is_deleted=False)


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ListUserSerializer

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
