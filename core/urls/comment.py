from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.comment import *

router = routers.DefaultRouter()   # url for class base view
router.register(r'', CommentViewSet, basename='CommentViewSet' )

app_name = 'comment'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),

   path('Comment-By-product/<int:product_id>/', CommentViewSet.as_view({'get': 'comments_by_product'}), name='comments_by_product'),
   path('Comment-By-user/<int:user_id>/', CommentViewSet.as_view({'get': 'comments_by_user'}), name='comments_by_user'),

]
