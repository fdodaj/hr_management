from rest_framework import serializers
from .models import Holiday


class ListHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['name', 'description', 'from_date', 'to_date', 'date_created', 'is_active']


class CreateHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['name', 'description', 'from_date', 'to_date']


class UpdateHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['name', 'description', 'from_date', 'to_date']


class HolidayDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['name', 'description', 'from_date', 'to_date', 'date_created', 'is_active']


class HoldaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'
