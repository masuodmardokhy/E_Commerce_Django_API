from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from core.models.shopping_cart import *                     # * it means all
from core.models.cart_item import Cart_Item                     # * it means all
from core.serializers.cart_item import *
from core.serializers.users import *
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

    def list(self, request, user_id=None):
        try:
            if user_id is not None:
                cart_items = Cart_Item.objects.filter(user=user_id)
            else:
                cart_items = Cart_Item.objects.all()

            shopping_cart_data = {'cart_items': cart_items}
            serializer = Shopping_CartListSerializer(shopping_cart_data)

            # Check if there are any changes in the request data
            if request.data:
                product_id = request.data.get('product_id')
                new_amount = request.data.get('new_amount')
                serializer.update_amount(product_id, new_amount)

            return Response(serializer.data)
        except Users.DoesNotExist:
            return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['patch'])
    def update_amount(self, request, user_id=None, id=None):
        try:
            shopping_cart = Shopping_Cart.objects.get(user=user_id)
            product = Product.objects.get(id=id)

            # Get the product ID and new amount from the request data
            product_id = request.data.get('product_id')
            new_amount = request.data.get('new_amount')

            # Update the amount in the shopping cart
            shopping_cart.update_amount(product_id, new_amount)

            serializer = Shopping_CartListSerializer(shopping_cart)
            return Response(serializer.data)
        except Shopping_Cart.DoesNotExist:
            return Response("Shopping Cart not found", status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='item_clear/(?P<id>\d+)')
    def item_clear(self, request, id=None):
        cart = Cart_Item(request)
        product = Product.objects.get(id=id)
        cart.remove(product)
        return Response("Product removed from cart successfully", status=status.HTTP_200_OK)


    # def list(self, request, user_id=None):
    #     try:
    #         if user_id is not None:
    #             cart_items = Cart_Item.objects.filter(user=user_id)
    #         else:
    #             cart_items = Cart_Item.objects.all()
    #
    #         shopping_cart_data = {'cart_items': cart_items}
    #         serializer = Shopping_CartListSerializer(shopping_cart_data)
    #
    #         return Response(serializer.data)
    #     except Users.DoesNotExist:
    #         return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)


    # def partial_update(self, request, pk=None):
    #     try:
    #         shopping_cart = Shopping_Cart.objects.get(pk=pk)
    #
    #         # Update the cart_items based on request.data
    #         cart_items_data = request.data.get('cart_items', [])
    #         for item_data in cart_items_data:
    #             item_id = item_data.get('id')
    #             amount = item_data.get('amount')
    #             if item_id is not None:
    #                 cart_item = Cart_Item.objects.get(pk=item_id, shopping_cart=shopping_cart)
    #                 cart_item.amount = amount
    #                 cart_item.save()
    #
    #         # Recalculate total_price, total_amount_item, and total_amount_product
    #         shopping_cart.total_price = shopping_cart.get_total_price()
    #         shopping_cart.total_amount_item = shopping_cart.get_total_amount_item()
    #         shopping_cart.total_amount_product = shopping_cart.get_total_amount_product()
    #         shopping_cart.save()
    #
    #         serializer = Shopping_CartSerializer(shopping_cart)
    #         return Response(serializer.data)
    #     except Shopping_Cart.DoesNotExist:
    #         return Response("Shopping Cart not found", status=status.HTTP_404_NOT_FOUND)
    #     except Cart_Item.DoesNotExist:
    #         return Response("Product not found in the shopping cart", status=status.HTTP_404_NOT_FOUND)
    #



    # def partial_update(self, request, user_id=None, product_id=None):
    #     try:
    #         shopping_cart = Shopping_Cart.objects.get(user=user_id)
    #         cart_item = Cart_Item.objects.get(shopping_cart=shopping_cart, product=product_id)
    #
    #         cart_item.save()
    #
    #         shopping_cart.total_price = shopping_cart.get_total_price()
    #         shopping_cart.total_amount_item = shopping_cart.get_total_amount_item()
    #         shopping_cart.total_amount_product = shopping_cart.get_total_amount_product()
    #         shopping_cart.save()
    #
    #         serializer = Shopping_CartListSerializer(shopping_cart)
    #         return Response(serializer.data)
    #
    #     except Shopping_Cart.DoesNotExist:
    #         return Response("Shopping Cart not found", status=status.HTTP_404_NOT_FOUND)
    #     except Cart_Item.DoesNotExist:
    #         return Response("Product not found in the shopping cart", status=status.HTTP_404_NOT_FOUND)



    # def partial_update(self, request, pk=None):
    #     shopping_cart = self.get_object()
    #     serializer = self.get_serializer(shopping_cart, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #

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