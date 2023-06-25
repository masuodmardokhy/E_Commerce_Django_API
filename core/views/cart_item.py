from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from core.models.cart_item import *
from core.serializers.cart_item import *


class Cart_ItemViewSet(viewsets.ModelViewSet):
    queryset = Cart_Item.objects.all()
    serializer_class = Cart_ItemSerializer


    def list(self, request, *args, **kwargs):
        cart_items = self.get_queryset()
        serializer = self.get_serializer(cart_items, many=True)
        return Response(serializer.data)
