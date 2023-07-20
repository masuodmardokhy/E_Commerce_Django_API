
from rest_framework import serializers
from core.models.category import Category
from core.serializers.product import ProductSerializer



class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    subcategories = serializers.SerializerMethodField()

    def get_subcategories(self, category):
        subcategories = category.subcategories.all()
        serializer = self.__class__(subcategories, many=True, context=self.context)
        return serializer.data

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'sub', 'products', 'subcategories']

class CategoryWithSubcategoriesSerializer(serializers.ModelSerializer):
    sub = serializers.SerializerMethodField()
    products = ProductSerializer(many=True)

    def get_sub(self, category):
        subcategories = category.subcategories.all()
        if subcategories:
            subcategories_data = CategoryWithSubcategoriesSerializer(subcategories, many=True, context=self.context).data
            for subcategory_data in subcategories_data:
                subcategory_data['sub'] = self.get_sub(Category.objects.get(id=subcategory_data['id']))
                subcategory_data['products'] = ProductSerializer(subcategory_data['products'], many=True).data
            return subcategories_data
        return []

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'sub', 'products']