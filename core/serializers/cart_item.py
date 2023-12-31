from rest_framework import serializers
from core.models.cart_item import *

class Cart_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Item
        fields = ('id','user','product','name', 'amount', 'price',)
