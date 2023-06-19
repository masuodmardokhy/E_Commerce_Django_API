from rest_framework.decorators import api_view          # viewsets for class base view
from rest_framework.response import Response
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from .models import *                                   # * it means all
from .serializers import *



class Shopping_CartViewSet(viewsets.ModelViewSet):
    queryset = Shopping_Cart.objects.all()
    serializer_class = Shapping_CartSerializer

    def list(self, request):
        shopping_cart = self.get_queryset()
        serializer = self.get_serializer(shopping_cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        shopping_cart = self.get_object()
        serializer = self.get_serializer(shopping_cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        shopping_cart = self.get_object()
        serializer = self.get_serializer(shopping_cart, data=request.data, partial=True)  # partial = True, This means that only the part of the data that needs to be updated
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            product = self.get_object()
            product.delete()
            return Response("Deleted product with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)
