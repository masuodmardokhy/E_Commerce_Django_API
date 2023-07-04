from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.shopping_cart import *



router = routers.DefaultRouter()        # url for class base view
router.register('shopping_cart_viewset',Shopping_CartViewSet),

app_name = "shopping_cart"
urlpatterns = [
                # url for function base view
    path('clear-cart', Shopping_CartViewSet.as_view({'get': 'clear_cart'}), name='clear_cart'),    # for clear all product as cart
    path('checkout', Shopping_CartViewSet.as_view({'get': 'checkout'}), name='checkout'),          # for checkout cart

]
urlpatterns += router.urls