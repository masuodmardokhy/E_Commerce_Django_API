from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from core.models.like_dislike import *
from core.models.users import *
from core.serializers.like_dislike import UserLikeSerializer
from rest_framework import viewsets
from rest_framework import status                      # for show messages
from rest_framework.decorators import action




class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 8


class Like_DislikeViewSet(viewsets.ModelViewSet):
    queryset = Like_Dislike.objects.all()
    serializer_class = UserLikeSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'create']  # The fields you want to enable ordering on
    search_fields = []  # The fields you want the search feature to be active on

    @action(detail=False, methods=['post'])
    def like(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')
        comment_id = request.data.get('comment_id')

        try:
            user = Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        existing_like = Like_Dislike.objects.filter(user=user, product=product).first()

        if existing_like:
            if existing_like.is_dislike:
                # Update the existing dislike to become a like
                existing_like.is_dislike = False
                existing_like.is_like = True
                existing_like.comment = comment_id
                existing_like.save()
            else:
                # User already liked, return a message
                return Response({'message': 'You have already liked this product'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Create a new like
            like_dislike = Like_Dislike.objects.create(
                user=user,
                product=product,
                comment=comment_id,
                is_like=True
            )

        return Response({'message': 'Liked successfully'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def dislike(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')
        comment_id = request.data.get('comment_id')

        try:
            user = Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        existing_dislike = Like_Dislike.objects.filter(user=user, product=product).first()

        if existing_dislike:
            if existing_dislike.is_like:
                # Update the existing like to become a dislike
                existing_dislike.is_like = False
                existing_dislike.is_dislike = True
                existing_dislike.comment = comment_id
                existing_dislike.save()
            else:
                # User already disliked, return a message
                return Response({'message': 'You have already disliked this product'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            # Create a new dislike
            like_dislike = Like_Dislike.objects.create(
                user=user,
                product=product,
                comment=comment_id,
                is_dislike=True
            )

        return Response({'message': 'Disliked successfully'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def unlike(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')

        try:
            user = Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        existing_like = Like_Dislike.objects.filter(user=user, product=product, is_like=True).first()

        if existing_like:
            existing_like.delete()
            return Response({'message': 'Unliked successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You have not liked this product'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def undislike(self, request):
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')

        try:
            user = Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        existing_dislike = Like_Dislike.objects.filter(user=user, product=product, is_dislike=True).first()

        if existing_dislike:
            existing_dislike.delete()
            return Response({'message': 'Undisliked successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'You have not disliked this product'}, status=status.HTTP_400_BAD_REQUEST)

