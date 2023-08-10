from rest_framework import serializers
from core.models.shopping_cart import *
from core.models.order import *
from core.serializers.cart_item import Cart_ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'