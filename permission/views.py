from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import DestroyAPIView
from employee.models import Employee


from . import serializers
# from django.contrib.auth.models import User
from .models import Permission


class GetPto(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.GetPto


def get_queryset(self):
    return Permission.objects.filter(is_deleted=False)


class ListPermission(generics.ListAPIView):
    queryset = get_queryset(serializers.ListPermissionSerializer)
    serializer_class = serializers.ListPermissionSerializer


class CreatePermission(generics.CreateAPIView):
    serializer_class = serializers.CreatePermissionSerializer


class PermissionDetail(generics.RetrieveAPIView):
    queryset = get_queryset(serializers.PermissionDetail)
    serializer_class = serializers.PermissionDetail

#
class UpdatePermission(generics.UpdateAPIView):
    queryset = get_queryset(serializers.UpdatePermissionSerializer)
    serializer_class = serializers.UpdatePermissionSerializer

    def update(self, request, *args, **kwargs):
        new_status = request.data.get('status')
        id = kwargs['pk']
        obj = Permission.objects.get(id=id)

        if obj.status == new_status:
            return

        obj.user.pto -= 1
        obj.user.save()
        return super(UpdatePermission, self).update(request=request, *args, **kwargs)


class PermissionDestroyAPIView(DestroyAPIView):
    queryset = get_queryset(serializers.PermissionSerializer)
    serializer_class = serializers.PermissionSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

