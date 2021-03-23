from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, get_object_or_404

from . import serializers
# from django.contrib.auth.models import User
from .models import Department, User, Holiday


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class HolidayList(generics.ListCreateAPIView):
    serializer_class = serializers.HolidaySerializer
    queryset = Holiday.objects.all()


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

