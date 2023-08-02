from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from core.models.address import *
from core.serializers.address import *
from django.shortcuts import get_object_or_404



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 5


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['create']  # The fields you want to enable ordering on
    search_fields = ['city', 'stat' ]  # The fields you want the search feature to be active on


    @action(detail=False, methods=['get'])
    def address_by_user(self, request, user_id=None):
        try:
            # find user by user_id , get_object_or_404 is for Retrieve a record from the database
            user = get_object_or_404(Users, id=user_id)

            address = Address.objects.filter(user=user)  # We filter all address by user
            if not address.exists():
                return Response("There is a user, but there are no address for this user.",
                                status=status.HTTP_404_NOT_FOUND)

            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)

        except Users.DoesNotExist:
            return Response("There is no user with this ID.", status=status.HTTP_404_NOT_FOUND)

        # In case of another error
        except Exception as e:
            return Response("The user ID is invalid.", status=status.HTTP_400_BAD_REQUEST)