from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.shopping_cart import *



router = routers.DefaultRouter()        # url for class base view
router.register('',Shopping_CartViewSet),


app_name = "shopping_cart"
urlpatterns = [
                # url for function base view
    path('<int:user_id>', Shopping_CartViewSet.as_view({'get': 'list'}), name='list'),
    path('TotalpriceAndDelivery/<int:user_id>/<int:shopping_cart_id>/<int:delivery_id>/', Shopping_CartViewSet.as_view({'get': 'get_shoppingcart_with_sendprice'}), name='get_shoppingcart_with_sendprice'),


]
urlpatterns += router.urls