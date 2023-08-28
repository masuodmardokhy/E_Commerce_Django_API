from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.category import *



router = routers.DefaultRouter()        # url for class base view
router.register(r'',CategoryViewSet, basename='category_view_set'),


urlpatterns = [       # url for function base view
    path('', include(router.urls)),
    path('delete_all_category/', CategoryViewSet.as_view({'post': 'delete_all_category'}), name='delete_all_category'),

]
urlpatterns += router.urls