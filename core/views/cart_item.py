from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from core.serializers.cart_item import *
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 8

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class Cart_ItemViewSet(viewsets.ModelViewSet):
    queryset = Cart_Item.objects.all()
    serializer_class = Cart_ItemSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'create', 'total_price']  # The fields you want to enable ordering on
    search_fields = ['name',]  # The fields you want the search feature to be active on



    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        # Apply ordering if requested
        cart = request.query_params.get('ordering')
        if cart in self.ordering_fields:
            queryset = queryset.order_by(cart)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



    def create(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        user_id = request.data.get('user_id')

        try:
            user = Users.objects.get(id=user_id)
            cart_item = Cart_Item.create_from_product(product, user, shopping_cart=None)
            return Response("Cart item created successfully", status=status.HTTP_201_CREATED)
        except Users.DoesNotExist:
            return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)