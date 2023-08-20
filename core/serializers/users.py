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





class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Users
        fields = ('id', 'user_name', 'email', 'first_name', 'last_name', 'phone', 'password', 'user_image', 'is_admin')
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users(**validated_data)
        user.set_password(password)  # set hash
        user.save()
        return user



class UserProfileUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = Users
        fields = ('id', 'user_name', 'email', 'first_name', 'last_name', 'phone', 'password', 'user_image', 'is_admin')



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()