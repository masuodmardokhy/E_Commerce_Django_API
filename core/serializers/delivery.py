from rest_framework import serializers
from core.models.delivery import *



class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'