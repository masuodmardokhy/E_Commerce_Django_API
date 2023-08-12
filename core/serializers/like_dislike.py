from rest_framework import serializers
from core.models.like_dislike import *

class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like_Dislike
        fields = '__all__'
