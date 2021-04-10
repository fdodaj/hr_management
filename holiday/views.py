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


#
# class Login(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = Token.validated_data['user']
#         token, created = username.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'user': CustomUserSerializer(user).data})
#
#
# class Logout(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         response = self.http_method_not_allowed(request, *args, **kwargs)
#         return response
#
#     def post(self, request, *args, **kwargs):
#         return self.logout(request)
#
#     def logout(self, request):
#         try:
#             request.user.auth_token.delete()
#         except (AttributeError, ObjectDoesNotExist) as e:
#             logger.exception(e)
#             logger.debug("Can't logout", exc_info=True)
#             raise e
#             response = Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
#             return response
