from rest_framework import serializers
from core.models.users import *

class UserManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserManager
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'user_name', 'email', 'first_name', 'last_name', 'phone', 'password','user_image', 'is_admin']


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()