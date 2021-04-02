from rest_framework import generics
from rest_framework.generics import DestroyAPIView

from . import serializers
from .models import Holiday


# filter deleted holidays
def get_queryset(self):
    return Holiday.objects.filter(is_deleted=False)


# Create Holiday
class CreateHoliday(generics.CreateAPIView):
    serializer_class = serializers.CreateHolidaySerializer


# List all holidays
class HolidayList(generics.ListAPIView):
    serializer_class = serializers.ListHolidaySerializer
    queryset = get_queryset(serializers.ListHolidaySerializer)


# Update holiday
class UpdateHoliday(generics.UpdateAPIView):
    serializer_class = serializers.UpdateHolidaySerializer

    def get_queryset(self):  # filter deleted holidays
        return Holiday.objects.filter(is_deleted=False)


# Get holiday by ID
class HolidayDetail(generics.RetrieveAPIView):
    serializer_class = serializers.HolidayDetailSerializer
    queryset = get_queryset(serializer_class)


# Delete holiday by id ->  soft delete
class HolidayDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.HolidaySerializer
    queryset = get_queryset(serializer_class)

    def perform_destroy(queryset, instance):
        instance.is_deleted = True
        instance.save()
