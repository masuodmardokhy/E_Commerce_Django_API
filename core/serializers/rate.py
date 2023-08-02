from rest_framework import serializers
from core.models.rate import Rate

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['id','user', 'product', 'rate']
