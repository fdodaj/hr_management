from .models import Request
from rest_framework import serializers
from employee.models import Employee
from holiday.models import Holiday



class GetDate(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['date']



class ListRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id','user', 'description', 'date_created', 'status', 'date']
        # fields = '__all__'


class RequestDetail(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['user', 'description', 'date_created', 'status']

class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['user', 'description','date']

class UpdateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['status' ]


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
