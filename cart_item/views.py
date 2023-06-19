from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from .models import *                                   # * it means all
from .serializers import *



class Cart_ItemViewSet(viewsets.ModelViewSet):
    queryset = Cart_Item.objects.all()
    serializer_class = Cart_ItemSerializer


    def list(self, request, *args, **kwargs):
        cart_items = self.get_queryset()
        serializer = self.get_serializer(cart_items, many=True)
        return Response(serializer.data)
