from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django.core.serializers.json import DjangoJSONEncoder
import json
from core.models.cart_item import Cart_Item                     # * it means all
from core.serializers.cart_item import *
from core.serializers.users import *
from core.serializers.shopping_cart import *
from core.models.order import Order
from core.models.delivery import *



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 5

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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
                shopping_cart_data = {'cart_items': cart_items}
                serializer = Shopping_CartListSerializer(shopping_cart_data)
            else:
                return Response("Enter user_id to get shopping cart.", status=status.HTTP_404_NOT_FOUND)

            # Check if there are any changes in the request data
            if request.data:
                product_id = request.data.get('product_id')
                new_amount = request.data.get('new_amount')
                serializer.update_amount(product_id, new_amount)

            # Get the calculated results from the serializer
            calculated_results = serializer.data

            # Create a dictionary to store the data for the cart_items field
            cart_items_data = {
                'user': user_id,
                'cart_items': calculated_results['cart_items'],
                'total_price': calculated_results['total_price'],
                'total_amount_item': calculated_results['total_amount_item'],
                'total_amount_product': calculated_results['total_amount_product']
            }

            # Convert the cart_items_data to JSON format
            cart_items_json = json.dumps(cart_items_data, cls=DjangoJSONEncoder)

            # Create or update the Shopping_Cart object for the user
            shopping_cart, _ = Shopping_Cart.objects.update_or_create(user_id=user_id,
                                                                      defaults={'cart_items': cart_items_json})

            #  total_price، total_amount_item و total_amount_product , Update
            shopping_cart.total_price = calculated_results['total_price']
            shopping_cart.total_amount_item = calculated_results['total_amount_item']
            shopping_cart.total_amount_product = calculated_results['total_amount_product']
            shopping_cart.save()

            return Response(serializer.data)
        except Users.DoesNotExist:
            return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)



    def get_shoppingcart_with_sendprice(self, request, user_id=None, shopping_cart_id=None, delivery_id=None):
        try:
            if user_id:
                shopping_carts = Shopping_Cart.objects.filter(user_id=user_id)
                if not shopping_carts.exists():
                    return Response("This user's shopping cart is empty", status=status.HTTP_404_NOT_FOUND)

                total_price_with_send_price = 0

                shopping_cart = Shopping_Cart.objects.get(pk=shopping_cart_id)
                total_price = shopping_cart.total_price

                delivery = Delivery.objects.get(pk=delivery_id)
                send_price = delivery.send_price

                for cart in shopping_carts:
                    total_price_with_send_price = total_price + send_price

                return Response({
                    "user_id": user_id,
                    "total_price ": total_price,
                    "send_price": send_price,
                    "total_price_with_send_price": total_price_with_send_price,
                })
            else:
                return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)
        except Shopping_Cart.DoesNotExist:
            return Response("Invalid shopping cart ID", status=status.HTTP_400_BAD_REQUEST)






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

