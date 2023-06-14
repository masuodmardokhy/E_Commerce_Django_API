from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from .models import *                                  # * it means all
from .serializers import *



class Sub_CategoryViewSet(viewsets.ModelViewSet):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer

