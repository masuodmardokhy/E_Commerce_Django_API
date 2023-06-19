from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .import views


router = routers.DefaultRouter()        # url for class base view
router.register('shopping_cart_viewset',views.Shopping_CartViewSet),

app_name = "shopping_cart"
urlpatterns = [
                # url for function base view
]
urlpatterns += router.urls