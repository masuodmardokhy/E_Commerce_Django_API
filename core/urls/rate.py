from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.rate import RateViewSet

router = routers.DefaultRouter()   # url for class base view
router.register(r'', RateViewSet, basename='RateViewSet' )

app_name = 'rate'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),


]