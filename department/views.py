from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import DestroyAPIView

from . import serializers
# from django.contrib.auth.models import User
from .models import Department


def get_queryset(self):
    return Department.objects.filter(is_deleted=False)


class ListDepartment(generics.ListAPIView):
    queryset = get_queryset(serializers.ListDepartmentSerializer)
    serializer_class = serializers.ListDepartmentSerializer


# create department
class CreateDepartment(generics.CreateAPIView):
    # queryset = get_queryset(serializers.CreateDepartmentSerializer)
    serializer_class = serializers.CreateDepartmentSerializer


# get deparment detail by ID
class DepartmentDetail(generics.RetrieveAPIView):
    queryset = get_queryset(serializers.DepartmentDetail)
    serializer_class = serializers.DepartmentDetail


# update department by ID
class UpdateDepartment(generics.UpdateAPIView):
    queryset = get_queryset(serializers.UpdateDepartmentSerializer)
    serializer_class = serializers.UpdateDepartmentSerializer


# (soft)delete department by ID
class DepartmentDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.DepartmentSerializer
    queryset = get_queryset(serializers.DepartmentSerializer)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
