from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core import views
from core.views.order import *
from core.views.order import OrderViewSet


router = routers.DefaultRouter()        # url for class base view
router.register(r'',OrderViewSet),

app_name = "order"
urlpatterns = [
    path('', include(router.urls)),
    path('<int:user_id>/<int:shopping_cart_id>/<int:delivery_id>/<int:address_id>/',OrderViewSet.as_view({'get': 'get_shoppingcart_with_delivery_move_to_order'}),name='get_shoppingcart_with_delivery_move_to_order'),


]
urlpatterns += router.urls