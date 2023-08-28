from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from core.serializers.category import *                # * it means all
from core.models.category import *
from rest_framework import filters
from rest_framework.filters import SearchFilter



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 8


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'create']  # The fields you want to enable ordering on
    search_fields = ['name',]  # The fields you want the search feature to be active on


    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        # Apply ordering if requested
        cat = request.query_params.get('ordering')
        if cat in self.ordering_fields:
            queryset = queryset.order_by(cat)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        cat = self.get_object()
        serializer = self.get_serializer(cat)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data,
                                         partial=True)  # partial = True, This means that only the part of the data that needs to be updated
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None):
        cat = self.get_object()
        serializer = self.get_serializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            cat = self.get_object()
            cat.delete()
            return Response("Deleted category with ID: {pk}", status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response("category not found", status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['delete'])
    def delete_all_category(self, request):
        deleted_count, _ = Category.objects.all().delete()
        return Response({'message': f'{deleted_count} category were deleted successfully.'})
