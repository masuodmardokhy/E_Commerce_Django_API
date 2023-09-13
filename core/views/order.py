from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from core.models.order import Order
from core.serializers.order import OrderSerializer
from core.models.shopping_cart import Shopping_Cart
from core.models.delivery import Delivery
from core.models.address import *



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 5


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'quantity']  # The fields you want to enable ordering on
    search_fields = ['name', ]  # The fields you want the search feature to be active on
    pagination_class = MyPagination


    def get_shoppingcart_with_delivery_move_to_order(self, request, user_id=None, shopping_cart_id=None, delivery_id=None, address_id=None):
        try:
            shopping_carts = Shopping_Cart.objects.filter(user_id=user_id, id=shopping_cart_id)
            if not shopping_carts.exists():
                return Response("This user's shopping cart is empty", status=status.HTTP_404_NOT_FOUND)

            total_price_with_send_price = 0

            shopping_cart = Shopping_Cart.objects.get(pk=shopping_cart_id)
            total_price = shopping_cart.total_price

            delivery = Delivery.objects.get(pk=delivery_id)
            send_price = delivery.send_price

            address = Address.objects.get(pk=address_id)

            for cart in shopping_carts:
                total_price_with_send_price = total_price + send_price

            order = Order(
                user_id=user_id,
                shopping_cart=shopping_cart,
                delivery=delivery,
                address=address,
                total_price=total_price,
                send_price=send_price,
                total_price_with_send_price=total_price_with_send_price
            )
            order.save()

            # shopping_carts.delete()

            return Response({

                "user_id": request.user.id,
                "total_price": total_price,
                "send_price": send_price,
                "total_price_with_send_price": total_price_with_send_price,
            })

        except Shopping_Cart.DoesNotExist:
            return Response("Invalid shopping cart ID", status=status.HTTP_400_BAD_REQUEST)


