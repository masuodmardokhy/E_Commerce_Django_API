from rest_framework import serializers
from core.models.shopping_cart import *
from core.serializers.cart_item import Cart_ItemSerializer

class Shopping_CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_Cart
        fields = ['id', 'order', 'user', 'total_price', 'total_amount_product', 'total_amount_item']


class Shopping_CartListSerializer(serializers.Serializer):
    def get_total_price(self, obj):
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])
        return sum(item['price'] for item in cart_items_data)
    def get_total_amount_product(self, obj):
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])
        return sum(item['product'] for item in cart_items_data)
    def get_total_amount_item(self, obj):
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])
        return len(cart_items_data)


    cart_items = Cart_ItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    total_amount_item = serializers.SerializerMethodField(method_name='get_total_amount_item')
    total_amount_product = serializers.SerializerMethodField(method_name='get_total_amount_product')
