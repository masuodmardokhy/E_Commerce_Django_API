from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.users import *


router = routers.DefaultRouter()   # url for class base view
router.register(r'', UserViewSet, basename='user_view_set' )



urlpatterns = [   # url for function base view
   path('filter/name/<str:name>/', UserViewSet.as_view({'get': 'filter_user_by_name'}), name='filter_user_by_id'),  # filter user by name API
   path('filter/id/<int:pk>/', UserViewSet.as_view({'get': 'filter_user_by_id'}),name='filter_user-by-id'),  # filter user by id API
   path('sign_in/', UserViewSet.as_view({'get': 'user_sign_in'}),name='user_sign_in'),  # user sign in API
   path('sign_out/', UserViewSet.as_view({'get': 'user_sign_out'}),name='user_sign_out'),  # user sign out API



]

urlpatterns += router.urls