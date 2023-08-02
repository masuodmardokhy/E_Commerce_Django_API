from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.rate import RateViewSet

router = routers.DefaultRouter()   # url for class base view
router.register(r'', RateViewSet, basename='RateViewSet' )

app_name = 'rate'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),
   path('rate_by_product/<int:product_id>/', RateViewSet.as_view({'get': 'rate_by_product'}), name='rate_by_product'),
   path('rate_by_user/<int:user_id>/', RateViewSet.as_view({'get': 'rate_by_user'}), name='rate_by_user'),

]