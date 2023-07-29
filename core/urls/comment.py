from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.comment import *

router = routers.DefaultRouter()   # url for class base view
router.register(r'', CommentViewSet, basename='CommentViewSet' )

app_name = 'comment'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),
]
