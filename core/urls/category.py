from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.category import *



router = routers.DefaultRouter()        # url for class base view
router.register('category_view_set',CategoryViewSet),

urlpatterns = [       # url for function base view

]
urlpatterns += router.urls