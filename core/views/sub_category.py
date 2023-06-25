from rest_framework.response import Response
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from core.models.sub_category import *                     # * it means all
from core.serializers.sub_category import *




# WE USE VIEWSETS AND SO WE CAN USE APIVIEW FOR MAKE THIS CLASS
class Sub_CategoryViewSet(viewsets.ModelViewSet):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer

    def list(self,request):
        sub_category = self.get_queryset()
        serializer = self.get_serializer(sub_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        sub_category = self.get_object()
        serializer = self.get_serializer(sub_category)
        return Response(serializer.data)

    def update(self, request, pk=None):
        sub_category = self.get_object()
        serializer = self.get_serializer(sub_category, data=request.data, partial=True)  # partial = True, This means that only the part of the data that needs to be updated
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            sub_category = self.get_object()
            sub_category.delete()
            return Response("Deleted product with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
        except sub_category.DoesNotExist:
            return Response("Product not found", status=status.HTTP_404_NOT_FOUND)
