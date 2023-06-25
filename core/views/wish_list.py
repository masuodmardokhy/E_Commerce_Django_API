from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from core.models.wish_list import *                     # * it means all
from core.models.shopping_cart import *                     # * it means all
from core.serializers.shopping_cart import *



class Wish_ListViewSet(viewsets.ModelViewSet):
    queryset = Shopping_Cart.objects.all()
    serializer_class = Shapping_CartSerializer