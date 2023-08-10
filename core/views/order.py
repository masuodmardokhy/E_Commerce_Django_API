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


    # # این متد را اضافه کنید
    # def list(self, request, *args, **kwargs):
    #     return self.get_shoppingcart_with_delivery_move_to_order(request, *args, **kwargs)
    #





    # def get_permissions(self):
    #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
    #         self.permission_classes = [IsAuthenticated]
    #     return super(OrderViewSet, self).get_permissions()


    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     # Apply ordering if requested
    #     ordering = request.query_params.get('ordering')
    #     if ordering in self.ordering_fields:
    #         queryset = queryset.order_by(ordering)
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    #
    #
    #
    # def retrieve(self, request, pk=None):
    #     queryset = self.get_queryset()
    #     order = self.get_object()
    #     serializer = self.get_serializer(order)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # def create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #
    # def update(self, request, pk=None):
    #     order = self.get_object()
    #     serializer = self.get_serializer(order, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # def partial_update(self, request, pk=None):
    #     order = self.get_object()
    #     serializer = self.get_serializer(order, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # def destroy(self, request, pk=None):
    #     try:
    #         order = self.get_object()
    #         order.delete()
    #         return Response(f"Deleted order with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
    #     except Order.DoesNotExist:
    #         return Response("Order not found", status=status.HTTP_404_NOT_FOUND)
    #
    #



#
# class MyPagination(PageNumberPagination):
#     page_size_query_param = 'size'
#     max_page_size = 10
#
#
# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     ordering_fields = ['name', 'quantity']  # The fields you want to enable ordering on
#     search_fields = ['name', ]  # The fields you want the search feature to be active on
#     pagination_class = MyPagination
#
#
#
#     # def get_permissions(self):
#     #     if self.action in ['create', 'update', 'partial_update', 'destroy']:
#     #         self.permission_classes = [IsAuthenticated]
#     #     return super(OrderViewSet, self).get_permissions()
#

# def list(self, request):
#     queryset = self.filter_queryset(self.get_queryset())
#
#     # Apply ordering if requested
#     ordering = request.query_params.get('ordering')
#     if ordering in self.ordering_fields:
#         queryset = queryset.order_by(ordering)
#
#     page = self.paginate_queryset(queryset)
#     if page is not None:
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)
#
#     serializer = self.get_serializer(queryset, many=True)
#     return Response(serializer.data)



#     def retrieve(self, request, pk=None):
#         queryset = self.get_queryset()
#         order = self.get_object()
#         serializer = self.get_serializer(order)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def create(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#     def update(self, request, pk=None):
#         order = self.get_object()
#         serializer = self.get_serializer(order, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def partial_update(self, request, pk=None):
#         order = self.get_object()
#         serializer = self.get_serializer(order, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
#     def destroy(self, request, pk=None):
#         try:
#             order = self.get_object()
#             order.delete()
#             return Response(f"Deleted order with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
#         except Order.DoesNotExist:
#             return Response("Order not found", status=status.HTTP_404_NOT_FOUND)
#
#
#     @action(detail=True, methods=['delete'])
#     def cancel_order(self, request, pk=None):
#         try:
#             order = self.get_object()
#             order.delete()
#             return Response(f"Cancelled order with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
#         except Order.DoesNotExist:
#             return Response("Order not found", status=status.HTTP_404_NOT_FOUND)






#  //// USE API VIEW ////
#  //// we can use API view for make order  and  we useing  def ( get ,post, put, delete ) for function////

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Order
# from .serializers import OrderSerializer
#
# class OrderAPIView(APIView):
#     def get(self, request):
#         queryset = Order.objects.all()
#         serializer = OrderSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         order = Order.objects.get(pk=pk)
#         serializer = OrderSerializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def delete(self, request, pk=None):
#         order = Order.objects.get(pk=pk)
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
