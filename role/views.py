from rest_framework import generics
from rest_framework.generics import DestroyAPIView

from . import serializers
from .models import Role


# filter deleted holidays
def get_queryset(self):
    return Role.objects.all()


# Create Holiday
class CreateRole(generics.CreateAPIView):
    queryset = get_queryset(serializers.ListRoleSerializer)
    serializer_class = serializers.CreateRoleSerializer


# List all holidays
class RoleList(generics.ListAPIView):
    serializer_class = serializers.ListRoleSerializer
    queryset = get_queryset(serializers.ListRoleSerializer)


# Update holiday
class UpdateRole(generics.UpdateAPIView):
    serializer_class = serializers.UpdateRoleSerializer
    queryset = get_queryset(serializers.UpdateRoleSerializer)


# Get holiday by ID
class RoleDetail(generics.RetrieveAPIView):
    serializer_class = serializers.RoleDetailSerializer
    queryset = get_queryset(serializers.RoleDetailSerializer)


