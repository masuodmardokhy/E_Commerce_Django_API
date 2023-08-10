from rest_framework import serializers
from core.models.product import *


class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField(source='calculate_total_price')  # for don't show field in create
    # slug = serializers.ReadOnlyField(source='save')

    class Meta:
        model = Product
        fields = ['id', 'create','update', 'name', 'slug', 'amount','color', 'size', 'unit_price', 'discount', 'total_price', 'available', 'description','images', 'users', 'category']



