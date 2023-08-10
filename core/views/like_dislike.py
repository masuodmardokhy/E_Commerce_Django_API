from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models.like_dislike import UserLike
from core.serializers.like_dislike import UserLikeSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_product(request):
    product_id = request.data.get('product_id')
    user = request.user

    like, created = UserLike.objects.get_or_create(user=user, product_id=product_id)
    like.is_like = not like.is_like
    like.is_dislike = False
    like.save()

    serializer = UserLikeSerializer(like)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dislike_product(request):
    product_id = request.data.get('product_id')
    user = request.user

    dislike, created = UserLike.objects.get_or_create(user=user, product_id=product_id)
    dislike.is_like = False
    dislike.is_dislike = not dislike.is_dislike
    dislike.save()

    serializer = UserLikeSerializer(dislike)
    return Response(serializer.data)
