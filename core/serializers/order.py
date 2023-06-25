from rest_framework import serializers
from core.models.order import *



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'