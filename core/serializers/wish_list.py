from rest_framework import serializers
from core.models.wish_list import *


class Wish_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish_List
        fields = '__all__'