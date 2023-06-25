from rest_framework import serializers
from core.models.base import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
