from rest_framework import serializers
from core.models.rate import *


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = '__all__'
