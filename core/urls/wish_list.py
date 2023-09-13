from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.wish_list import *


router = routers.DefaultRouter()   # url for class base view
router.register(r'', Wish_ListViewSet, basename='wish_list_view_set' )



app_name = "users"
urlpatterns = [   # url for function base view
   path('', include(router.urls)),
   path('delete_all_wishlist', Wish_ListViewSet.as_view({'post': 'delete_all_wishlist'}), name='delete_all_wishlist'),
   # path('add_to_wishlist/<int:user_id>/<int:pk>/', Wish_ListViewSet.as_view({'post': 'add_to_wishlist'}),name='add_to_wishlist'),

]

urlpatterns += router.urls