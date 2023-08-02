from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status                       # for show messages
from rest_framework import viewsets , permissions       # viewsets for class base view
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from core.models.rate import *
from core.serializers.rate import *
from django.shortcuts import get_object_or_404
from django.db.models import Avg


class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 5


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = MyPagination
    filter_backends = [SearchFilter, filters.OrderingFilter]
    ordering_fields = ['create']  # The fields you want to enable ordering on
    search_fields = []  # The fields you want the search feature to be active on


    def create(self, request, *args, **kwargs):
        try:
            # Check if the user has already voted for this product
            product_id = request.data.get('product')
            user_id = request.data.get('user')
            existing_rate = Rate.objects.filter(product_id=product_id, user_id=user_id).first()

            if existing_rate:
                # If the user has already voted, replace the new vote with the previous one
                existing_rate.rate = request.data.get('rate')
                existing_rate.save()
                serializer = RateSerializer(existing_rate)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                # If the user has not voted for this product, create a new vote
                serializer = RateSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Product.DoesNotExist:
            return Response("There is no product with this ID.", status=status.HTTP_404_NOT_FOUND)

        # In case of another error
        except Exception as e:   # Exception as e:it means "If any kind of error occurs, store it in variable e and execute the following block"
            return Response("An error occurred.", status=status.HTTP_400_BAD_REQUEST)



    @action(detail=False, methods=['get'])
    def rate_by_product(self, request, product_id=None):
        try:
            # find product by product_id , get_object_or_404 is for Retrieve a record from the database
            product = get_object_or_404(Product, id=product_id)

            rates = Rate.objects.filter(product_id=product_id)

            # Calculate the number of rate
            num_rates = rates.count()

            # Calculation of total rate
            total_rate = rates.aggregate(total_rate=Avg('rate'))['total_rate']

            # Calculation of average scores
            avg_rate = total_rate / num_rates if num_rates > 0 else 0

            response_data = {
                "num_rates": num_rates,
                "total_rate": total_rate,
                "avg_rate": avg_rate,
                "rates": RateSerializer(rates, many=True).data,
            }

            return Response(response_data)

        except Exception as e:
            return Response("The product ID is invalid.", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def rate_by_user(self, request, user_id=None):
        try:
            # find product by user_id , get_object_or_404 is for Retrieve a record from the database
            user = get_object_or_404(Users, id=user_id)

            rates = Rate.objects.filter(user_id=user_id)

            # Calculate the number of rate
            num_rates = rates.count()

            # Calculation of total rate
            total_rate = rates.aggregate(total_rate=Avg('rate'))['total_rate']

            # Calculation of average scores
            avg_rate = total_rate / num_rates if num_rates > 0 else 0

            response_data = {
                "num_rates": num_rates,
                "total_rate": total_rate,
                "avg_rate": avg_rate,
                "rates": RateSerializer(rates, many=True).data,
            }

            return Response(response_data)

        except Exception as e:
            return Response("The user ID is invalid.", status=status.HTTP_400_BAD_REQUEST)



