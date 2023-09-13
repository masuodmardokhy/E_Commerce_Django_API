from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from core.models.comment import *
from core.serializers.comment import *
from django.shortcuts import get_object_or_404




class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 5


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = [ 'create']  # The fields you want to enable ordering on
    search_fields = []  # The fields you want the search feature to be active on



    def list(self, request, *args, **kwargs):
        comments = self.queryset
        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None, *args, **kwargs):
        comment = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, pk=None, *args, **kwargs):
        comment = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None, *args, **kwargs):
        comment = get_object_or_404(self.queryset, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=False, methods=['get'])
    def comments_by_product(self, request, product_id=None):
        try:
            # find product by product_id , get_object_or_404 is for Retrieve a record from the database
            product = get_object_or_404(Product, id=product_id)

            comments = Comment.objects.filter(product_id=product_id)    # We filter all comments by product_id
            if not comments.exists():
                return Response("There is a product, but there are no comments for this product.", status=status.HTTP_404_NOT_FOUND)

            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        except Product.DoesNotExist:
            return Response("There is no product with this ID.", status=status.HTTP_404_NOT_FOUND)

        #In case of another error
        except Exception as e:
            return Response("The product ID is invalid.", status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'])
    def comments_by_user(self, request, user_id=None):
        try:
            # find user by user_id , get_object_or_404 is for Retrieve a record from the database
            product = get_object_or_404(Users, id=user_id)

            comments = Comment.objects.filter(user_id=user_id)    # We filter all comments by user_id
            if not comments.exists():
                return Response("There is a user, but there are no comments for this user.", status=status.HTTP_404_NOT_FOUND)

            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        except Product.DoesNotExist:
            return Response("There is no user with this ID.", status=status.HTTP_404_NOT_FOUND)

        #In case of another error
        except Exception as e:
            return Response("The user ID is invalid.", status=status.HTTP_400_BAD_REQUEST)

