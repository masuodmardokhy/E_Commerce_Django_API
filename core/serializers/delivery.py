from rest_framework import serializers
from core.models.delivery import *
from core.serializers.d import Cart_ItemSerializer


class DeliverySerializer(serializers.ModelSerializer):
    shopping_cart = Shopping_CartSerializer()

    class Meta:
        model = Delivery
        fields = ['shopping_cart', 'total_amount_product', 'send_to_out_Capital', 'send_price', 'total_price', 'calculate_total_price']
