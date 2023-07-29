from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.address import *

router = routers.DefaultRouter()   # url for class base view
router.register(r'', AddressViewSet, basename='AddressViewSet' )

app_name = 'address'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),


]