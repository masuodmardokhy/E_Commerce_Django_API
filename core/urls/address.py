from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.address import *

router = routers.DefaultRouter()   # url for class base view
router.register(r'', AddressViewSet, basename='AddressViewSet' )

app_name = 'address'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),
   path('address_by_user/<int:user_id>/', AddressViewSet.as_view({'get': 'address_by_user'}), name='address_by_user'),

]