from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets , permissions
from core.models.wish_list import *
from core.serializers.wish_list import *
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework.decorators import action


class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 8



class Wish_ListViewSet(viewsets.ModelViewSet):
    queryset = Wish_List.objects.all()
    serializer_class = Wish_ListSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name', 'total_price']  # The fields you want to enable ordering on
    search_fields = ['name', ]  # The fields you want the search feature to be active on



    @action(detail=False, methods=['delete'])
    def delete_all_wishlist(self, request):
        deleted_count, _ = Wish_List.objects.all().delete()
        return Response({'message': f'{deleted_count} wish list were deleted successfully.'})
