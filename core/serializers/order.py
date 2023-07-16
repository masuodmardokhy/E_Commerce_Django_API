from rest_framework import serializers
from core.models.shopping_cart import *
from core.serializers.cart_item import Cart_ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields = ['user', 'total_price', 'total_amount_product', 'total_amount_item']

    total_price_ = serializers.SerializerMethodField()
    total_amount_product = serializers.SerializerMethodField(method_name='get_total_amount_product')


    def get_total_price(self, obj):                                                       # obj['cart_items']: A list of shopping cart items
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])  # Convert the data in obj['cart items'] to display
        return sum(item['price'] for item in cart_items_data)
    def get_total_amount_product(self, obj):
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])
        return sum(item['product'] for item in cart_items_data)
