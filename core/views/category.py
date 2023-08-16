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
    ordering_fields = ['name', 'create', 'total_price']  # The fields you want to enable ordering on
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




    # @action(detail=False, methods=['GET'])
    # def unique_categories(self, request):
    #     categories = self.get_queryset()
    #     serialized_data = []
    #     shown_categories = {}
    #
    #     for category in categories:
    #         if category.id not in shown_categories:
    #             serializer = self.get_serializer(category)
    #             serialized_data.append(serializer.data)
    #             shown_categories[category.id] = True
    #
    #     return Response({
    #         'count': len(serialized_data),
    #         'results': serialized_data,
    #     })
    #

    # @action(detail=False, methods=['get'])
    # def get_category_tree(self, request, *args, **kwargs):
    #     top_level_categories = Category.objects.filter(sub__isnull=True)
    #     serializer = CategoryWithSubcategoriesSerializer(top_level_categories, many=True, context={'request': request})
    #     return Response(serializer.data)
    #




    # def get_sub(self, category):
    #     subcategories = category.sub.all()
    #     print("Category:", category.name, "Subcategories:", subcategories)
    #     if subcategories:
    #         subcategories_data = CategoryWithSubcategoriesSerializer(subcategories, many=True).data
    #         for subcategory_data in subcategories_data:
    #             print("Subcategory Data:", subcategory_data)
    #             subcategory_data['sub'] = self.get_sub(category)
    #             subcategory_data['products'] = ProductSerializer(category.products.all(), many=True).data
    #         return subcategories_data
    #     return []

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     sub_cat_id = data.get('sub_cat', None)
    #
    #     # If sub_cat_id exists, try to get the related Category record
    #     if sub_cat_id:
    #         try:
    #             sub_category = Category.objects.get(id=sub_cat_id)
    #         except Category.DoesNotExist:
    #             return Response({'detail': 'Invalid sub category ID.'}, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         sub_category = None
    #
    #     serializer = CategorySerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # Create a new Category instance with the serializer data
    #     category = serializer.save(sub_cat=sub_category)
    #
    #     return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #
    #     # name filtering
    #     name = request.query_params.get('name')
    #     if name:
    #         queryset = queryset.filter(name__icontains=name)
    #
    #     # price filtering
    #     price = request.query_params.get('price')
    #     if price:
    #         queryset = queryset.filter(price=price)
    #
    #     # sort by name , date , price_lowest , price_highest
    #     sort_by = request.query_params.get('sort_by')
    #     if sort_by == 'name':
    #         queryset = queryset.order_by('name')
    #     elif sort_by == 'date':
    #         queryset = queryset.order_by('create')
    #
    #     # paginations
    #     paginator = self.pagination_class()
    #     page = paginator.paginate_queryset(queryset, request)
    #     serializer = self.get_serializer(page, many=True)
    #     return paginator.get_paginated_response(serializer.data)
    #


    #
    # @action(detail=True, methods=['get'])
    # def filter_category_by_name(self, request, name=None):
    #     try:
    #         cat = Category.objects.filter(name=name)
    #         serializer = CategorySerializer(cat, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Category.DoesNotExist:
    #         return Response("category not found", status=status.HTTP_404_NOT_FOUND)
    #
    #
    # @action(detail=True, methods=['get'])
    # def filter_category_by_id(self, request, pk=None):
    #     try:
    #         cat = Category.objects.get(id=pk)
    #         serializer = CategorySerializer(cat)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Category.DoesNotExist:
    #         return Response("category not found", status=status.HTTP_404_NOT_FOUND)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_category_by_date(self, request):
    #     start_date = request.query_params.get('start_date')
    #     end_date = request.query_params.get('end_date')
    #     categories = self.get_queryset().filter(date__range=[start_date, end_date])
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_category_first_created(self, request):   # aggregate is a method for operation sum,count,avg, min,max
    #     earliest_created = self.get_queryset().aggregate(earliest_created=Min('create')).get('earliest_created')
    #     categories = self.get_queryset().filter(create=earliest_created)
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_category_last_created(self, request):
    #     latest_created = self.get_queryset().aggregate(latest_created=Max('create')).get('latest_created')
    #     categories = self.get_queryset().filter(create=latest_created).order_by('create')
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_category_last_to_first_created(self, request):
    #     categories = self.get_queryset().order_by('-create')
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_category_first_to_last_created(self, request):
    #     categories = self.get_queryset().order_by('create')
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def search_category_by_name(self, request, search_param):
    #     categories = self.get_queryset().filter(name__icontains=search_param)
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #



# /////////////////////




    # in the class view set make list,create,retrive,destroy, update,partial update automatic
    # and dont have need we make that


    # # @action(detail=False, methods=['get'])
    # def list(self, request):
    #     category = self.get_queryset()
    #     serializer = self.get_serializer(category, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # # @action(detail=False, methods=['post'])
    # def create(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # # @action(detail=True, methods=['put'])
    # def retrieve(self, request, pk=None):
    #     # try:
    #     #     cat = Category.objects.get(id=pk)
    #     #     serializer = CategorySerializer(cat, data=request.data)
    #     #     if serializer.is_valid():
    #     #         serializer.save()
    #     #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     # except Category.DoesNotExist:
    #     #     return Response("this category not found", status=status.HTTP_404_NOT_FOUND)
    #     order = self.get_object()
    #     serializer = self.get_serializer(order, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    #
    #
    # # @action(detail=True, methods=['delete'])
    # def destroy(self, request, pk=None):
    #     try:
    #         cat = Category.objects.get(id=pk)
    #         cat.delete()
    #         return Response("category deleted", status=status.HTTP_204_NO_CONTENT)
    #     except Category.DoesNotExist:
    #         return Response("category not found", status=status.HTTP_404_NOT_FOUND)
