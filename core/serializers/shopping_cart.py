from rest_framework import serializers
from core.models.shopping_cart import *
from core.serializers.cart_item import Cart_ItemSerializer

# class Shopping_CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Shopping_Cart
#         fields = ['id', 'user', 'delivery', 'total_price', 'total_amount_product', 'total_amount_item']

class Shopping_CartSerializer(serializers.ModelSerializer):
    cart_items = Cart_ItemSerializer(many=True, read_only=True)
    calculated_total_price = serializers.SerializerMethodField()

    class Meta:
        model = Shopping_Cart
        fields = ['id', 'user', 'delivery', 'total_price', 'total_amount_item', 'total_amount_product', 'calculated_total_price', 'cart_items']

    def get_calculated_total_price(self, obj):
        return sum(item.price for item in obj.cart_items)


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
        return sum(item['product'] for item in cart_items_data)
    def get_total_amount_item(self, obj):
        cart_items_data = self.fields['cart_items'].to_representation(obj['cart_items'])
        return len(cart_items_data)



    # def update_amount(self, product_id, new_amount):
    #     # Get the cart items data
    #     cart_items_data = self.fields['cart_items'].to_representation(self.instance['cart_items'])
    #
    #     # Find the cart item with the specified product ID
    #     for item in cart_items_data:
    #         if item['product'] == product_id:
    #             item['amount'] = new_amount
    #             break
    #
    #     # Update the total_amount_item
    #     total_amount_item = sum(item['amount'] for item in cart_items_data)
    #
    #     # Update the total_amount_product
    #     total_amount_product = len(set(item['product'] for item in cart_items_data))
    #
    #     # Update the instance data
    #     self.instance['cart_items'] = cart_items_data
    #     self.instance['total_amount_item'] = total_amount_item
    #     self.instance['total_amount_product'] = total_amount_product
    #
    #     return self.instance
