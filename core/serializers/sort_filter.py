from rest_framework import serializers

class SortFilterSerializer(serializers.Serializer):
    sort_by = serializers.CharField(max_length=30)
