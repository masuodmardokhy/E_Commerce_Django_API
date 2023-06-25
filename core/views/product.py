from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from core.models.product import *                     # * it means all
from core.serializers.product import *
from django.db.models import Min, Max


# WE USE VIEWSETS AND AT THE END OF THESE CODES  , WE CREATED THIS CLASS USING APIVIEW AND COMMENTED IT.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    @action(detail=False, methods=['get'])
    def list_product(self, request):
        product = self.get_queryset()
        serializer = self.get_serializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['post'])
    def create_product(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['put'])
    def update_product(self, request, pk=None):
        try:
            user = Product.objects.get(id=pk)
            serializer = ProductSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            return Response("user not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['delete'])
    def delete_product(self, request, pk=None):
        try:
            user = Product.objects.get(id=pk)
            user.delete()
            return Response("user deleted", status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response("user not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['get'])
    def filter_product_by_name(self, request, name=None):
        try:
            users = Product.objects.filter(first_name=name)
            serializer = ProductSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['get'])
    def filter_product_min_total_price(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        min_price = queryset.aggregate(min_price=Min('total_price')).get('min_price')
        if min_price is not None:
            queryset = queryset.filter(total_price=min_price)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['get'])
    def filter_product_max_total_price(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        max_price = queryset.aggregate(max_price=Max('total_price')).get('max_price')
        if max_price is not None:
            queryset = queryset.filter(total_price=max_price)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





#  //// USE API VIEW ////
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class ProductAPIView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
