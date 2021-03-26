from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import DestroyAPIView

from . import serializers
# from django.contrib.auth.models import User
from .models import Department


class ListDepartment(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.ListDepartmentSerializer

    def get_queryset(self):
        user = self.request.user
        return Department.objects.filter(is_deleted=False)


class CreateDepartment(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.CreateDepartmentSerializer


class DepartmentDetail(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentDetail

    def get_queryset(self):
        user = self.request.user
        return Department.objects.filter(is_deleted=False)


class UpdateDepartment(generics.UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.UpdateDepartmentSerializer

class DepartmentDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.DepartmentSerializer
    permission_classes = []
    queryset = Department.objects.all()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()