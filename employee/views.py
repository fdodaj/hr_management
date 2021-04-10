from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .serializers import UserSerializer

User = get_user_model()


def get_queryset(self):
    return User.objects.filter(is_deleted=False)


# Create user with authenicated password
class CreateUser(generics.CreateAPIView):
    queryset = get_queryset(serializers.UserSerializer)
    serializer_class = serializers.UserSerializer

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = Employee.objects.create(
            email=email,
            username=username,
            password=make_password(password))
        return user


# lsit all users that are not deleted
class ListUser(generics.ListAPIView):
    queryset = get_queryset(serializers.ListUserSerializer)
    serializer_class = serializers.ListUserSerializer
    permission_classes = [IsAuthenticated]


# get user with ID
class UserDetail(RetrieveAPIView):
    queryset = get_queryset(serializers.UserDetailSerializer)
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [IsAuthenticated]


# update user by ID
class UpdateView(UpdateAPIView):
    queryset = get_queryset(serializers.UpdateUserSerializer)
    serializer_class = serializers.UpdateUserSerializer
    permission_classes = [IsAuthenticated]


# (soft)Delete an user
class UserDestroyAPIView(DestroyAPIView):
    queryset = get_queryset(serializers.UserSerializer)
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()


# view user password
class UserPasswordView(RetrieveAPIView):
    queryset = get_queryset(serializers.UserPasswordSerializer)
    serializer_class = serializers.UserPasswordSerializer
    permission_classes = [IsAuthenticated]


class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})


class Logout(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        response = self.http_method_not_allowed(request, *args, **kwargs)
        return response

    def post(self, request, *args, **kwargs):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except(AttributeError, ObjectDoesNotExist) as e:
            logger.exception(e)
            logger.debug("Can't logout", exc_info=True)
            raise e
            response = Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        return response
