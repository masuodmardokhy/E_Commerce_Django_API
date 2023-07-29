from rest_framework import serializers
from core.models.comment import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'




