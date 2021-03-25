from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, UpdateAPIView

from . import serializers
# from django.contrib.auth.models import User
from .models import User


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UpdateUserSerializer
