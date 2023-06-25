from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.product import *


router = routers.DefaultRouter()   # url for class base view
router.register(r'', ProductViewSet, basename='user_view_set' )


urlpatterns = [   # url for function base view
   path('', include(router.urls)),
   path('list/', ProductViewSet.as_view({'get': 'list_product'}), name='list_product'),  # list product API
   path('create/', ProductViewSet.as_view({'get': 'create_product'}), name='create_product'),   # create product(sign up) API
   path('update/id/<int:pk>/',ProductViewSet.as_view({'get': 'update_product'}), name='update_product'),  # update product API
   path('delete/id/<int:pk>/',ProductViewSet.as_view({'get': 'delete_product'}), name='delete_product'),  # delete product API
   path('filter/name/<str:name>/', ProductViewSet.as_view({'get': 'filter_product_by_name'}), name='filter_product_by_name'),  # filter product by name API
   path('filter/min-price/', ProductViewSet.as_view({'get': 'filter_product_min_total_price'}),name='filter_product_min_total_price'),  # filter product by min total price API
   path('filter/max-price/', ProductViewSet.as_view({'get': 'filter_product_max_total_price'}),name='filter_product_max_total_price'),  # filter product max total price API

]

urlpatterns += router.urls