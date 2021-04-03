from rest_framework import serializers


from .models import Role


#list user serializer
class ListRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CreateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UpdateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

#user detail seializer
class RoleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

#update user serializer
class UpdateRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

# #delete user serializer
# class DeleteRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Role
#         fields = ['is_deleted']

# create user serializer
# class RoleSerializer(ModelSerializer):
#     class Meta:
#         model = Role
#         fields = '__all__'


