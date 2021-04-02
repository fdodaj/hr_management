from rest_framework import serializers
from rest_framework.generics import DestroyAPIView
from rest_framework.serializers import ModelSerializer

from employee.models import Employee


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name', 'username', 'email', 'password', 'role', "user_id"]
        fields = '__all__'


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name', 'email', 'date_created', 'hire_date', 'role', 'id']
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name', 'email', 'date_created', 'hire_date', 'role']
        fields = '__all__'

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['first_name', 'last_name', 'password', 'role']
        fields = '__all__'

# class DeleteUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = ['is_deleted']
#         fields = '__all__'



class UserSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class UserPasswordSerializer(ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['password']
        fields = '__all__'

class UpdatePasswordSerializer(ModelSerializer):
    class Meta:
        model = Employee
        # fields = ['password']
        fields = '__all__'