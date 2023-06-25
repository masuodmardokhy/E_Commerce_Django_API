from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.wish_list import *


router = routers.DefaultRouter()   # url for class base view
router.register(r'wish_list_view_set', Wish_ListViewSet, basename='wish_list_view_set' )



app_name = "users"
urlpatterns = [   # url for function base view
   path('', include(router.urls)),

]

urlpatterns += router.urls