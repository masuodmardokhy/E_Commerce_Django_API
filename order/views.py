from rest_framework.viewsets import ModelViewSet
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
from rest_framework.response import Response

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        order = self.get_object()
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)






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
