from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import DestroyAPIView
from employee.models import Employee
from django.http import JsonResponse



from . import serializers
# from django.contrib.auth.models import User
from .models import Request


class GetPto(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializers.GetPto


def get_queryset(self):
    return Request.objects.filter(is_deleted=False)


class ListRequest(generics.ListAPIView):
    queryset = get_queryset(serializers.ListRequestSerializer)
    serializer_class = serializers.ListRequestSerializer


class CreateRequest(generics.CreateAPIView):
    serializer_class = serializers.CreateRequestSerializer


class RequestDetail(generics.RetrieveAPIView):
    queryset = get_queryset(serializers.RequestDetail)
    serializer_class = serializers.RequestDetail

#
class UpdateRequest(generics.UpdateAPIView):
    queryset = get_queryset(serializers.UpdateRequestSerializer)
    serializer_class = serializers.UpdateRequestSerializer

    def update(self, request, *args, **kwargs):
        new_status = request.data.get('status')
        id = kwargs['pk']
        obj = Request.objects.get(id=id) # objekti qe merr nga databaza


        if obj.status == new_status:
            return

        if new_status == "Accepted":
            if obj.user.pto < 1:
                 return JsonResponse("You don't have any PTO left",safe = False)
            else:
                obj.user.pto -= 1
                obj.user.save()
                return super(UpdateRequest, self).update(request=request, *args, **kwargs)
        elif new_status == "Denied":
            return super(UpdateRequest, self).update(request=request, *args, **kwargs)
            return JsonResponse("You denied this request", safe=False)
        else:
            return JsonResponse("Enter a valid status,", safe=False)

class RequestDestroyAPIView(DestroyAPIView):
    queryset = get_queryset(serializers.RequestSerializer)
    serializer_class = serializers.RequestSerializer

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

