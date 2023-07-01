from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from core.models.product import *
from core.serializers.product import *                # * it means all
from django.db.models import Min, Max
from django import forms



class SortForm(forms.Form):
    CHOICES = [
        ('name', 'نام'),
        ('lowest_price', 'کمترین قیمت'),
        ('highest_price', 'بیشترین قیمت'),
    ]
    sort_by = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 10

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination


    def list(self, request, *args, **kwargs):
        # Create and handle the form
        form = SortForm(request.GET)
        if form.is_valid():
            sort_by = form.cleaned_data['sort_by']
            queryset = Product.objects.all()
            if sort_by == 'name':
                queryset = queryset.order_by('name')
            elif sort_by == 'lowest_price':
                queryset = queryset.order_by('price')
            elif sort_by == 'highest_price':
                queryset = queryset.order_by('-price')
            else:
                # Handle invalid sort option
                return Response({'error': 'Invalid sort option'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Handle form validation errors
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

        # Apply additional filters
        name = request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        price = request.query_params.get('price')
        if price:
            queryset = queryset.filter(price=price)

        # Perform pagination
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)





    @action(detail=True, methods=['get'])
    def filter_product_by_name(self, request, name=None):
        try:
            prod = Product.objects.filter(name=name)
            serializer = ProductSerializer(prod, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response("category not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['get'])
    def filter_product_by_id(self, request, pk=None):
        try:
            prod = Product.objects.get(id=pk)
            serializer = ProductSerializer(prod)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response("category not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['get'])
    def filter_product_by_date(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        categories = self.get_queryset().filter(date__range=[start_date, end_date])
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_product_first_created(self, request):    # aggregate is a method for operation sum,count,avg, min,max
        earliest_created = self.get_queryset().aggregate(earliest_created=Min('create')).get('earliest_created')
        categories = self.get_queryset().filter(create=earliest_created)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_product_last_created(self, request):
        latest_created = self.get_queryset().aggregate(latest_created=Max('create')).get('latest_created')
        categories = self.get_queryset().filter(create=latest_created).order_by('create')
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_product_last_to_first_created(self, request):
        categories = self.get_queryset().order_by('-create')
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_product_first_to_last_created(self, request):
        categories = self.get_queryset().order_by('create')
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def search_product_by_name(self, request, search_param):
        categories = self.get_queryset().filter(name__icontains=search_param)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)









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
