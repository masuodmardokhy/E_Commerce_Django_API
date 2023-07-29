from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from core.models.address import *
from core.serializers.address import *

class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 5


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'create']  # The fields you want to enable ordering on
    search_fields = ['name', ]  # The fields you want the search feature to be active on
