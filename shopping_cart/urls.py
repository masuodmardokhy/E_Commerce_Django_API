from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .import views


router = routers.DefaultRouter()        # url for class base view
router.register('shapping_cart_view_set',views.Shopping_CartViewSet),

app_name = "shapping_cart"
urlpatterns = [
                # url for function base view
]
urlpatterns += router.urls