from rest_framework import serializers
from core.models.shopping_cart import *


class Shapping_CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shopping_Cart
        fields = '__all__'
