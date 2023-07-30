from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from core.serializers.product import *                # * it means all
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from core.models.users import *
from core.models.cart_item import *



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 8



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'create', 'total_price']  # The fields you want to enable ordering on
    search_fields = ['name',]  # The fields you want the search feature to be active on


    @action(detail=False, methods=['delete'])
    def delete_all_products(self, request):
        deleted_count, _ = Product.objects.all().delete()
        return Response({'message': f'{deleted_count} products were deleted successfully.'})


    @action(detail=True, methods=['post'], url_path='add-to-cart')
    def add_to_cart(self, request, pk=None, user_id=None):
        product = self.get_object()
        amount = request.data.get('amount')
        name = product.name
        total_price = product.calculate_total_price

        try:
            user = Users.objects.get(id=user_id)
            # if isinstance(user,AnonymousUser):
            #     user=None
            # if user.is_anonymous:
            #     return Response("Unauthorized", status=status.HTTP_401_UNAUTHORIZED)
            cart_item = Cart_Item.objects.get(user=user, product=product)
            cart_item.amount += amount
            cart_item.save()

        except Users.DoesNotExist:
            return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)

        except Cart_Item.DoesNotExist:
            # Create a new cart item for the product
            cart_item = Cart_Item.objects.create(user=user, product=product, amount=amount, name=name, price=total_price)

        return Response("Added to cart successfully", status=status.HTTP_200_OK)



    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        # Apply ordering if requested
        product = request.query_params.get('ordering')
        if product in self.ordering_fields:
            queryset = queryset.order_by(product)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        product = self.get_object()
        serializer = self.get_serializer(product)
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
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data, partial=True)
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
            return Response("product not found", status=status.HTTP_404_NOT_FOUND)





# @action(detail=False, methods=['get'])
    # def sort_filter_form(self, request):
    #     form = Sort_FilterForm()
    #     return Response({'form': form.as_ul()})
    #
    #
    # @action(detail=False, methods=['get'])
    # def sort_filter(self, request):
    #     form = Sort_FilterForm(request.POST)
    #     if form.is_valid():
    #         sort_by = form.cleaned_data['sort_by']
    #         queryset = self.get_queryset()
    #         if sort_by == 'name':
    #             queryset = queryset.order_by('name')
    #         elif sort_by == 'lowest_price':
    #             queryset = queryset.order_by('price')
    #         elif sort_by == 'highest_price':
    #             queryset = queryset.order_by('-price')
    #         else:
    #             # Handle invalid sort option
    #             return Response({'error': 'Invalid sort option'}, status=status.HTTP_400_BAD_REQUEST)
    #         page = self.paginate_queryset(queryset)
    #         if page is not None:
    #             serializer = self.get_serializer(page, many=True)
    #             return self.get_paginated_response(serializer.data)
    #         serializer = self.get_serializer(queryset, many=True)
    #         return Response(serializer.data)
    #     else:
    #         # Handle form validation errors
    #         return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    #




#     @action(detail=True, methods=['post'])
#     def list_filter_sort(self, request, *args, **kwargs):
#         # Create and handle the form
#         form = SortForm(request.GET)
#         if form.is_valid():
#             sort_by = form.cleaned_data['sort_by']
#             queryset = Product.objects.all()
#             if sort_by == 'name':
#                 queryset = queryset.order_by('name')
#             elif sort_by == 'lowest_price':
#                 queryset = queryset.order_by('price')
#             elif sort_by == 'highest_price':
#                 queryset = queryset.order_by('-price')
#             else:
#                 # Handle invalid sort option
#                 return Response({'error': 'Invalid sort option'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # Handle form validation errors
#             return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         # Apply additional filters
#         name = request.query_params.get('name')
#         if name:
#             queryset = queryset.filter(name__icontains=name)
#
#         price = request.query_params.get('price')
#         if price:
#             queryset = queryset.filter(price=price)
#
#         # Perform pagination
#         paginator = self.pagination_class()
#         page = paginator.paginate_queryset(queryset, request)
#         serializer = self.get_serializer(page, many=True)
#         return paginator.get_paginated_response(serializer.data)
#
#
#

    #
    #
    # @action(detail=True, methods=['get'])
    # def filter_product_by_name(self, request, name=None):
    #     try:
    #         prod = Product.objects.filter(name=name)
    #         serializer = ProductSerializer(prod, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Product.DoesNotExist:
    #         return Response("category not found", status=status.HTTP_404_NOT_FOUND)
    #
    #
    # @action(detail=True, methods=['get'])
    # def filter_product_by_id(self, request, pk=None):
    #     try:
    #         prod = Product.objects.get(id=pk)
    #         serializer = ProductSerializer(prod)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Product.DoesNotExist:
    #         return Response("category not found", status=status.HTTP_404_NOT_FOUND)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_product_by_date(self, request):
    #     start_date = request.query_params.get('start_date')
    #     end_date = request.query_params.get('end_date')
    #     categories = self.get_queryset().filter(date__range=[start_date, end_date])
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_product_first_created(self, request):    # aggregate is a method for operation sum,count,avg, min,max
    #     earliest_created = self.get_queryset().aggregate(earliest_created=Min('create')).get('earliest_created')
    #     categories = self.get_queryset().filter(create=earliest_created)
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_product_last_created(self, request):
    #     latest_created = self.get_queryset().aggregate(latest_created=Max('create')).get('latest_created')
    #     categories = self.get_queryset().filter(create=latest_created).order_by('create')
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_product_last_to_first_created(self, request):
    #     categories = self.get_queryset().order_by('-create')
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def filter_product_first_to_last_created(self, request):
    #     categories = self.get_queryset().order_by('create')
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['get'])
    # def search_product_by_name(self, request, search_param):
    #     categories = self.get_queryset().filter(name__icontains=search_param)
    #     serializer = self.get_serializer(categories, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    #
    #
    #




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
