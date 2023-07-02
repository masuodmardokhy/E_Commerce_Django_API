from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.product import *


router = routers.DefaultRouter()   # url for class base view
router.register(r'', ProductViewSet, basename='user_view_set' )


urlpatterns = [   # url for function base view
   path('', include(router.urls)),

    path('a', ProductViewSet.as_view({'get': 'list'}), name='product-list'), # list filtering sort by and pagination


    path('filter/name/<str:name>/', ProductViewSet.as_view({'get': 'filter_product_by_name'}),
        name='filter_product_by_name'),  # filter product by name API

   path('filter/id/<int:pk>/', ProductViewSet.as_view({'get': 'filter_product_by_id'}),
        name='filter_product_by_id'),  # filter product
   path('filter/first-created/', ProductViewSet.as_view({'get': 'filter_product_first_created'}),
        name='filter_product_first_created'),  # filter product first created API

   path('filter/last-created/', ProductViewSet.as_view({'get': 'filter_product_last_created'}),
        name='filter_product_last_created'),  # filter product last created API

   path('filter/lastToFirst-created/',ProductViewSet.as_view({'get': 'filter_product_last_to_first_created'}),
        name='filter_product_last_to_first_created'),  # filter product last to first created API

   path('filter/firstToLast-created/',ProductViewSet.as_view({'get': 'filter_product_first_to_last_created'}),
        name='filter_product_first_to_last_created'),  # filter product last to first created API

   path('search/<str:search_param>', ProductViewSet.as_view({'get': 'search_product_by_name'}),
        name='search_product_by_name'),  # search product by name API


]

urlpatterns += router.urls