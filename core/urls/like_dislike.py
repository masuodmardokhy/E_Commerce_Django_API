from core.views.like_dislike import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.like_dislike import *


router = routers.DefaultRouter()        # url for class base view
router.register(r'',Like_DislikeViewSet),

app_name = "like_dislike"
urlpatterns = [
    path('', include(router.urls)),
    path('like',Like_DislikeViewSet.as_view({'post': 'like'}),name='like'),
    path('unlike',Like_DislikeViewSet.as_view({'post': 'unlike'}),name='unlike'),
    path('dislike',Like_DislikeViewSet.as_view({'post': 'dislike'}),name='dislike'),
    path('undislike',Like_DislikeViewSet.as_view({'post': 'undislike'}),name='undislike'),


]
urlpatterns += router.urls
