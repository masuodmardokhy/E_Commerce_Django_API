from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from .models import *                                  # * it means all
from .serializers import *



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

