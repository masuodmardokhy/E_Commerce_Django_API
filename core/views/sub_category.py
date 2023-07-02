from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from core.models.category import *
from core.serializers.sub_category import *                # * it means all
from django.db.models import Min, Max



class MyPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 10



class Sub_CategoryViewSet(viewsets.ModelViewSet):
    queryset = Sub_Category.objects.all()
    serializer_class = Sub_CategorySerializer
    pagination_class = MyPagination



    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # name filtering
        name = request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        # price filtering
        price = request.query_params.get('price')
        if price:
            queryset = queryset.filter(price=price)

        # sort by name , date , price_lowest , price_highest
        sort_by = request.query_params.get('sort_by')
        if sort_by == 'name':
            queryset = queryset.order_by('name')
        elif sort_by == 'date':
            queryset = queryset.order_by('create')
        elif sort_by == 'price_lowest':
            queryset = queryset.order_by('price')
        elif sort_by == 'price_highest':
            queryset = queryset.order_by('-price')

        # paginations
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)




    @action(detail=True, methods=['get'])
    def filter_sub_category_by_name(self, request, name=None):
        try:
            sub = Sub_Category.objects.filter(name=name)
            serializer = Sub_CategorySerializer(sub, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Sub_Category.DoesNotExist:
            return Response("category not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['get'])
    def filter_sub_category_by_id(self, request, pk=None):
        try:
            sub = Sub_Category.objects.get(id=pk)
            serializer = Sub_CategorySerializer(sub)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Sub_Category.DoesNotExist:
            return Response("category not found", status=status.HTTP_404_NOT_FOUND)


    @action(detail=False, methods=['get'])
    def filter_sub_category_by_date(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        categories = self.get_queryset().filter(date__range=[start_date, end_date])
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_sub_category_first_created(self, request):    # aggregate is a method for operation sum,count,avg, min,max
        earliest_created = self.get_queryset().aggregate(earliest_created=Min('create')).get('earliest_created')
        categories = self.get_queryset().filter(create=earliest_created)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_sub_category_last_created(self, request):
        latest_created = self.get_queryset().aggregate(latest_created=Max('create')).get('latest_created')
        categories = self.get_queryset().filter(create=latest_created).order_by('create')
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_sub_category_last_to_first_created(self, request):
        categories = self.get_queryset().order_by('-create')
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def filter_sub_category_first_to_last_created(self, request):
        categories = self.get_queryset().order_by('create')
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def search_sub_category_by_name(self, request, search_param):
        categories = self.get_queryset().filter(name__icontains=search_param)
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    from django.db.models import F

