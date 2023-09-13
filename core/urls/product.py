from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.product import *


router = routers.DefaultRouter()   # url for class base view
router.register(r'', ProductViewSet, basename='ProductViewSet' )
app_name = 'core'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),

   path('add_to_cart/<int:user_id>/<int:pk>', ProductViewSet.as_view({'post': 'add_to_cart'}), name='add_to_cart'),
   path('delete_all_products', ProductViewSet.as_view({'post': 'delete_all_products'}), name='delete_all_products'),
   path('add_to_wishlist/<int:user_id>/<int:pk>', ProductViewSet.as_view({'post': 'add_to_wishlist'}), name='add_to_wishlist'),

 ]

urlpatterns += router.urls