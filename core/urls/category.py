from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.category import *



router = routers.DefaultRouter()        # url for class base view
router.register(r'',CategoryViewSet, basename='category_view_set'),


urlpatterns = [       # url for function base view
    path('', include(router.urls)),
    path('filter/name/<str:name>/', CategoryViewSet.as_view({'get': 'filter_category_by_name'}), name='filter_category_by_name'),                    #  filter category by name API
    path('filter/id/<int:pk>/', CategoryViewSet.as_view({'get': 'filter_category_by_id'}), name='filter_category_by_id'),                            #  filter category by id API
    # path('filter/date/', CategoryViewSet.as_view({'get': 'filter_category_by_date'}), name='filter_category_by_date'),                             #  filter category by data API
    path('filter/first-created/', CategoryViewSet.as_view({'get': 'filter_category_first_created'}), name='filter_category_first_created'),          # filter category first created API
    path('filter/last-created/', CategoryViewSet.as_view({'get': 'filter_category_last_created'}), name='filter_category_last_created'),             # filter category last created API
    path('filter/lastToFirst-created/', CategoryViewSet.as_view({'get': 'filter_category_last_to_first_created'}), name='filter_category_last_to_first_created'),      # filter category last to first created API
    path('filter/firstToLast-created/', CategoryViewSet.as_view({'get': 'filter_category_first_to_last_created'}), name='filter_category_first_to_last_created'),      # filter category last to first created API
    path('search/<str:search_param>', CategoryViewSet.as_view({'get': 'search_category_by_name'}), name='search_category_by_name'),                  # search category by name API


]
urlpatterns += router.urls