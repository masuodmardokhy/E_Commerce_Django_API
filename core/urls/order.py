from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core import views
from core.views.order import *


router = routers.DefaultRouter()        # url for class base view
router.register('order_view_set',OrderViewSet),

app_name = "order"
urlpatterns = [
                # url for function base view
]
urlpatterns += router.urls