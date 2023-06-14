from rest_framework import serializers
from .models import *

class Sub_CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_Category
        fields = '__all__'
