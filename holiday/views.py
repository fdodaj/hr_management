from rest_framework import generics
from . import serializers
from .models import Holiday


class HolidayList(generics.ListCreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = serializers.HolidaySerializer


class UpdateHoliday(generics.UpdateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = serializers.HolidaySerializer


class HolidayDetail(generics.RetrieveAPIView):
    queryset = Holiday.objects.all()
    serializer_class = serializers.UpdateHolidaySerializer
