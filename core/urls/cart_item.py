from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.cart_item import *


router = routers.DefaultRouter()        # url for class base view
router.register('cart_item_view_set',Cart_ItemViewSet),

app_name = "cart_item"
urlpatterns = [
                # url for function base view
]
urlpatterns += router.urls