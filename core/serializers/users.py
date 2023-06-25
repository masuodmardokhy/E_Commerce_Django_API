from rest_framework import serializers
from core.models.users import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'