from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
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
from core.models.wish_list import *
from core.serializers.wish_list import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, parsers


class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 8


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'create', 'total_price']  # The fields you want to enable ordering on
    search_fields = ['name',]  # The fields you want the search feature to be active on
    parser_classes = (parsers.MultiPartParser, parsers.FormParser) #Parsers for parsing data uploaded from HTTP requests



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


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        product_serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if product_serializer.is_valid():
            product = product_serializer.save()

            # add image to product
            images = request.FILES.getlist('images')
            for image in images:
                product_image = ProductImage.objects.create(product=product, image=image)

            return Response(product_serializer.data)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            return Response(f"Deleted product", status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response("product not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['delete'])
    def delete_all_products(self, request):
        deleted_count, _ = Product.objects.all().delete()
        return Response({'message': f'{deleted_count} products were deleted successfully.'})


    @action(detail=True, methods=['post'], url_path='add-to-cart')
    def add_to_cart(self, request, pk=None, user_id=None):
        product = self.get_object()
        amount = int(request.data.get('amount'))  # تبدیل amount به عدد
        name = product.name
        total_price = product.calculate_total_price

        try:
            user = Users.objects.get(id=user_id)

            # Get the number of product from the database
            product_stock = product.amount

            if amount > product_stock:
                return Response("Not enough stock available", status=status.HTTP_400_BAD_REQUEST)

            cart_item, created = Cart_Item.objects.get_or_create(
                user=user, product=product, defaults={'amount': amount, 'name': name, 'price': total_price}
            )

            if not created:
                cart_item.amount += amount
                cart_item.save()

            return Response("Added to cart successfully", status=status.HTTP_200_OK)

        except Users.DoesNotExist:
            return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)



    # @action(detail=True, methods=['post'], url_path='add-to-cart')
    # def add_to_cart(self, request, pk=None, user_id=None):
    #     product = self.get_object()
    #     amount = request.data.get('amount')
    #     name = product.name
    #     total_price = product.calculate_total_price
    #
    #     try:
    #         user = Users.objects.get(id=user_id)
    #         cart_item = Cart_Item.objects.get(user=user, product=product)
    #         cart_item.amount += int(amount)
    #         cart_item.save()
    #
    #     except Users.DoesNotExist:
    #         return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)
    #
    #     except Cart_Item.DoesNotExist:
    #         # Create a new cart item for the product
    #         cart_item = Cart_Item.objects.create(user=user, product=product, amount=amount, name=name, price=total_price)
    #
    #     return Response("Added to cart successfully", status=status.HTTP_200_OK)
    #

    @action(detail=True, methods=['post'], url_path='add-to-wishlist')
    def add_to_wishlist(self, request, pk=None, user_id=None):
        product = self.get_object()
        try:
            user = Users.objects.get(id=user_id)
            # Checking if the product is in the user's wish list or not
            if Wish_List.objects.filter(users=user, product=product).exists():
                return Response("The product is already in the wishlist.", status=status.HTTP_409_CONFLICT)
            # Add product to wish list
            wishlist_item = Wish_List.objects.create(users=user, product=product)
            serializer = Wish_ListSerializer(wishlist_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Users.DoesNotExist:
            return Response("Invalid user ID", status=status.HTTP_400_BAD_REQUEST)



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
