from rest_framework import serializers
from core.models.like_dislike import UserLike

class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLike
        fields = '__all__'
