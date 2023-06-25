from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.users import *


router = routers.DefaultRouter()   # url for class base view
router.register(r'user_view_set', UserViewSet, basename='user_view_set' )



urlpatterns = [   # url for function base view
   path('', include(router.urls)),
   path('user_view_set/list_user/', UserViewSet.as_view({'get': 'list_user'}), name='list_user'),  # list user API
   path('user_view_set/create_user/', UserViewSet.as_view({'get': 'create_user'}), name='create_user'),   # create user(sign up) API
   path('user_view_set/delete_user/<int:pk>/',UserViewSet.as_view({'get': 'destroy_user'}), name='destroy_user'),  # delete user API
   path('user_view_set/filter_user_by_name/<str:name>/', UserViewSet.as_view({'get': 'filter_user_by_name'}), name='filter_user_by_id'),  # filter user by name API
   path('user_view_set/filter_user_by_id/<int:pk>/', UserViewSet.as_view({'get': 'filter_user_by_id'}),name='filter_user-by-id'),  # filter user by id API
   path('user_view_set/user_sign_in/', UserViewSet.as_view({'get': 'user_sign_in'}),name='user_sign_in'),  # user sign in API
   path('user_view_set/user_sign_out/', UserViewSet.as_view({'get': 'user_sign_out'}),name='user_sign_out'),  # user sign out API



]

urlpatterns += router.urls