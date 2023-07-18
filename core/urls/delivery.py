from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core import views
from core.views.delivery import *


router = routers.DefaultRouter()        # url for class base view
router.register(r'',DeliveryViewSet, basename='DeliveryViewSet'),

app_name = "delivery"
urlpatterns = [
                # url for function base view
]
urlpatterns += router.urls