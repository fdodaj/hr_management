from rest_framework import serializers

from .models import Holiday


class ListHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['id', 'name', 'description', 'date']


class CreateHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['name', 'description', 'date']


class UpdateHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['name', 'description', 'date']


class HolidayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['id','name', 'description', 'date', 'date_created']


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'
