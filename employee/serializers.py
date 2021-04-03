from rest_framework import serializers
from rest_framework.generics import DestroyAPIView
from rest_framework.serializers import ModelSerializer

from employee.models import Employee


#list user serializer
class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['roles','password', 'id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'department', 'pto']

#user detail seializer
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'department', 'pto']

#update user serializer
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['username', 'first_name', 'last_name']

#delete user serializer
class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['is_deleted']

# create user serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['roles','username', 'password', 'first_name', 'last_name', 'email', 'department', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

#get password serilizer
class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['password']

#
# class UpdatePasswordSerializer(ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['password']
