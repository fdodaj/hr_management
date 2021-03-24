from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, get_object_or_404

from . import serializers
# from django.contrib.auth.models import User
from .models import User


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
