from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .import views


router = routers.DefaultRouter()        # url for class base view
router.register('product_view_set',views.ProductViewSet, basename='product_view_set'),

app_name = "product"
urlpatterns = [
                # url for function base view
]
urlpatterns += router.urls