from rest_framework import serializers
from core.models.delivery import Delivery
from core.serializers.shopping_cart import Shopping_CartSerializer


class DeliverySerializer(serializers.ModelSerializer):
    # shopping_cart = Shopping_CartSerializer(read_only=True, fields=['total_price', 'total_amount_product'])
    class Meta:
        model = Delivery
        fields = '__all__'


