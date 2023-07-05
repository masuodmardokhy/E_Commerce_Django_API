from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from core.models.delivery import *                     # * it means all
from core.serializers.delivery import *



class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer