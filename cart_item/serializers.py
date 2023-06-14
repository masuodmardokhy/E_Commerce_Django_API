from rest_framework import serializers
from .models import *

class Cart_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
