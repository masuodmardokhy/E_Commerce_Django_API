from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.shopping_cart import *



router = routers.DefaultRouter()        # url for class base view
router.register('',Shopping_CartViewSet),

app_name = "shopping_cart"
urlpatterns = [
                # url for function base view
    path('clear-cart', Shopping_CartViewSet.as_view({'get': 'clear_cart'}), name='clear_cart'),    # for clear all product as cart
    path('checkout/<int:pk>', Shopping_CartViewSet.as_view({'get': 'checkout'}), name='checkout'),          # for checkout cart
    path('<int:user_id>', Shopping_CartViewSet.as_view({'get': 'list'}), name='list'),
    path('<int:id>/a', Shopping_CartViewSet.as_view({'patch': 'update_amount'}), name='update_amount'),
    path('item_clear/<int:id>', Shopping_CartViewSet.as_view({'post': 'item_clear'}), name='item_clear'),

]
urlpatterns += router.urls