from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from .models import *                                  # * it means all
from .serializers import *



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        category = self.get_queryset()
        serializer = self.get_serializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        category = self.get_object()
        serializer = self.get_serializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        category = self.get_object()
        serializer = self.get_serializer(category, data=request.data, partial=True)  # partial = True, This means that only the part of the data that needs to be updated
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            category = self.get_object()
            category.delete()
            return Response("Deleted category                                                                                                                                                          with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)

