from rest_framework import generics
from rest_framework.generics import DestroyAPIView

from . import serializers
from .models import Holiday


class CreateHoliday(generics.CreateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = serializers.CreateHolidaySerializer


class HolidayList(generics.ListAPIView):
    queryset = Holiday.objects.all()
    serializer_class = serializers.ListHolidaySerializer

    def get_queryset(self):
        holiday = self.request.user
        return Holiday.objects.filter(is_deleted=False)


class UpdateHoliday(generics.UpdateAPIView):
    queryset = Holiday.objects.all()
    serializer_class = serializers.UpdateHolidaySerializer


class HolidayDetail(generics.RetrieveAPIView):
    queryset = Holiday.objects.all()
    serializer_class = serializers.HolidayDetailSerializer

    def get_queryset(self):
        user = self.request.user
        return Holiday.objects.filter(is_deleted=False)


class HoldayDestroyAPIView(DestroyAPIView):
    serializer_class = serializers.HoldaySerializer
    permission_classes = []
    queryset = Holiday.objects.all()

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
