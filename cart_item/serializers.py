from rest_framework import serializers
from .models import *

class Cart_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Item
        fields = '__all__'
