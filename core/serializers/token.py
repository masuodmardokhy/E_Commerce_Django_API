from rest_framework import serializers
from core.models.token import Token

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['user', 'token']
