from django.shortcuts import render
from .models import user
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]