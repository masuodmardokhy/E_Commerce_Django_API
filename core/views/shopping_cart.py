from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from core.models.shopping_cart import *                     # * it means all
from core.models.shopping_cart import Shopping_Cart                   # * it means all
from core.serializers.shopping_cart import *
from core.models.order import Order
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 5


class Shopping_CartViewSet(viewsets.ModelViewSet):
    queryset = Shopping_Cart.objects.all()
    serializer_class = Shopping_CartSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'create']  # The fields you want to enable ordering on
    search_fields = ['name', ]  # The fields you want the search feature to be active on


    def list(self, request, *args, **kwargs):
        shopping_carts = self.get_queryset()
        data = []
        for cart in shopping_carts:
            cart_data = {
                'user': cart.user_id,
                'total_price': cart.total_price,
                'total_amount': cart.total_amount,
                'list_cartitem': [item.id for item in cart.list_cartitem.all()]
            }
            data.append(cart_data)

        return Response(data)


    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     # Apply ordering if requested
    #     shopp = request.query_params.get('ordering')
    #     if shopp in self.ordering_fields:
    #         queryset = queryset.order_by(shopp)
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)



    def retrieve(self, request, pk=None):
        shopping_cart = self.get_object()
        serializer = self.get_serializer(shopping_cart)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        shopping_cart = self.get_object()
        serializer = self.get_serializer(shopping_cart, data=request.data, partial=True)  # partial = True, This means that only the part of the data that needs to be updated
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        shopping_cart = self.get_object()
        serializer = self.get_serializer(shopping_cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            shopp = self.get_object()
            shopp.delete()
            return Response("Deleted cart with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
        except Shopping_Cart.DoesNotExist:
            return Response("cart not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['post'])
    def clear_cart(self, request, pk=None):
        try:
            shopping_cart = self.get_object()
            shopping_cart.products.clear()
            return Response("The shopping cart has been successfully emptied.", status=status.HTTP_200_OK)
        except Shopping_Cart.DoesNotExist:
            return Response("Cart not found.", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        try:
            shopping_cart = self.get_object()

            # Create a new order
            order = Order.objects.create()

            # Moving cart products to order
            order.products.set(shopping_cart.products.all())

            # Calculation of the total price and the total amount of the order
            total_price = sum(product.price for product in order.products.all())
            total_amount = sum(product.amount for product in order.products.all())

            # Update cart details
            shopping_cart.order = order
            shopping_cart.total_price = total_price
            shopping_cart.total_amount = total_amount
            shopping_cart.save()

            # Remove cart products
            shopping_cart.products.clear()

            return Response("The order was successfully.", status=status.HTTP_200_OK)
        except Shopping_Cart.DoesNotExist:
            return Response("Cart not found.", status=status.HTTP_404_NOT_FOUND)



    # @action(detail=True, methods=['post'], url_path='cart_add/(?P<id>\d+)')
    # def cart_add(self, request, id=None):
    #     cart = Cart_Item(request)
    #     product = Product.objects.get(id=id)
    #     cart.add(product=product)
    #     return Response("Product added to cart successfully", status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='item_clear/(?P<id>\d+)')
    def item_clear(self, request, id=None):
        cart = Cart_Item(request)
        product = Product.objects.get(id=id)
        cart.remove(product)
        return Response("Product removed from cart successfully", status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='item_increment/(?P<id>\d+)')
    def item_increment(self, request, id=None):
        cart = Cart_Item(request)
        product = Product.objects.get(id=id)
        cart.add(product=product)
        return Response("Product quantity incremented successfully", status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='item_decrement/(?P<id>\d+)')
    def item_decrement(self, request, id=None):
        cart = Cart_Item(request)
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
        return Response("Product quantity decremented successfully", status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='cart_clear')
    def cart_clear(self, request):
        cart = Cart_Item(request)
        cart.clear()
        return Response("Cart cleared successfully", status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='cart_detail')
    def cart_detail(self, request):
        return Response("Cart detail view", status=status.HTTP_200_OK)