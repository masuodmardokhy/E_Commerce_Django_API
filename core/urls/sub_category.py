from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.sub_category import *



router = routers.DefaultRouter()        # url for class base view
router.register('sub_category_view_set', Sub_CategoryViewSet, basename='sub_category_view_set'),

app_name = "sub_category"
urlpatterns = [       # url for function base view

]
urlpatterns += router.urls