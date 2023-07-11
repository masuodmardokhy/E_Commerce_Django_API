from rest_framework import serializers
from core.models.shopping_cart import *
from core.serializers.cart_item import Cart_ItemSerializer


class Shopping_CartSerializer(serializers.ModelSerializer):
    cart_items = Cart_ItemSerializer(many=True, read_only=True)  # اضافه کردن رابطه cart_items

    class Meta:
        model = Shopping_Cart
        fields = ('user', 'order', 'total_amount', 'total_price', 'cart_items')  # فیلدهای مربوط به Shopping_Cart و رابطه cart_items را اینجا قرار دهید

