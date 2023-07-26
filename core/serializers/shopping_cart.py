from rest_framework import serializers
from core.models.shopping_cart import *
from core.serializers.cart_item import Cart_ItemSerializer

class Shopping_CartSerializer(serializers.ModelSerializer):
    cart_items = Cart_ItemSerializer(many=True, read_only=True)
    calculated_total_price = serializers.SerializerMethodField()

    class Meta:
        model = Shopping_Cart
        fields = ['id', 'user', 'delivery', 'total_price', 'total_amount_item', 'total_amount_product', 'calculated_total_price', 'cart_items' ]


    # def get_calculated_total_price(self, instance):
    #     return instance.total_price


    # def get_calculated_total_price(self, obj):
    #     delivery_send_price = obj.delivery.send_price  # مقدار 'send_price' مربوط به این مدل 'Shopping_Cart' را به دست می‌آوریم
    #     return obj.total_price + delivery_send_price  # مقدار 'total_price' اصلی را با 'send_price' جمع کرده و برمی‌گردانیم

class Shopping_CartListSerializer(serializers.Serializer):
    cart_items = Cart_ItemSerializer(many=True,)
    total_price = serializers.SerializerMethodField()
    total_amount_item = serializers.SerializerMethodField(method_name='get_total_amount_item')
    total_amount_product = serializers.SerializerMethodField(method_name='get_total_amount_product')


    def get_total_price(self, obj):                                                       # obj['cart_items']: A list of shopping cart items
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])  # Convert the data in obj['cart items'] to display
        return sum(item['price'] for item in cart_items_data)

    def get_total_amount_product(self, obj):
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])
        return sum(item['amount'] for item in cart_items_data)

    def get_total_amount_item(self, obj):
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])
        return len(cart_items_data)






