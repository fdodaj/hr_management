from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Department


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
