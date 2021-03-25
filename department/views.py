from django.shortcuts import render
from rest_framework import generics

from . import serializers
# from django.contrib.auth.models import User
from .models import Department


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class DepartmentDetail(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class UpdateDepartment(generics.UpdateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.UpdateDepartmentSerializer
