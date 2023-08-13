from rest_framework import serializers
from core.models.product import *


# Define the serializer for ProductImage model
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # Calculate the total_price field based on a method in the model
    total_price = serializers.ReadOnlyField(source='calculate_total_price')  # for don't show field in create
    # slug = serializers.ReadOnlyField(source='save')
    # Define the relationship with ProductImage model
    product_productimage = ProductImageSerializer(many=True, read_only=True)
    # Allow uploading multiple images
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'create','update', 'name', 'slug', 'amount','color', 'size', 'unit_price', 'discount',
                  'total_price', 'available', 'description', 'product_productimage', 'uploaded_images', 'user', 'category']

    # Override the create method to handle image uploads
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)
        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)
        return product

