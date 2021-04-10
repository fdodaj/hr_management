from .models import Request
from rest_framework import serializers
from employee.models import Employee

class GetPto(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['pto']



class ListRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id','user', 'description', 'date_created', 'status']
        # fields = '__all__'


class RequestDetail(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['user', 'description', 'date_created', 'status']

class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['user', 'description']

class UpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['status']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
