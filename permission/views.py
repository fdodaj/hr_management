from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import DestroyAPIView

from . import serializers
# from django.contrib.auth.models import User
from .models import Permission


class ListPermission(generics.ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = serializers.ListPermissionSerializer

    def get_queryset(self):
        user = self.request.user
        return Permission.objects.filter(is_deleted=False)


class CreatePermission(generics.CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = serializers.CreatePermissionSerializer


class PermissionDetail(generics.RetrieveAPIView):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionDetail

    def get_queryset(self):
        user = self.request.user
        return Permission.objects.filter(is_deleted=False)


class UpdatePermission(generics.UpdateAPIView):
    queryset = Permission.objects.all()
    serializer_class = serializers.UpdatePermissionSerializer


class PermissionDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.PermissionSerializer
    permission_classes = []
    queryset = Permission.objects.all()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
