from .models import Department
from rest_framework import serializers

#list all department serializer
class ListDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'department_leader', 'date_created']

#department detail serializer
class DepartmentDetail(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'department_leader', 'date_created']

#create department serializer
class CreateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name', 'department_leader']

#update department serialiizer
class UpdateDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['name','department_leader', ]

#department serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
