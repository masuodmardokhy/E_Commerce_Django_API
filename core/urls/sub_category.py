# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework import routers
# from core.views.sub_category import *
#
#
#
# router = routers.DefaultRouter()        # url for class base view
# router.register(r'', Sub_CategoryViewSet, basename='sub_category_view_set'),
#
# urlpatterns = [       # url for function base view
#     path('', include(router.urls)),
#
#     path('a', Sub_CategoryViewSet.as_view({'get': 'list_filter_sort'}), name='sub_category-list'),  # list filtering sort by and pagination
#
#     path('filter/name/<str:name>/', Sub_CategoryViewSet.as_view({'get': 'filter_sub_category_by_name'}),
#          name='filter_sub_category_by_name'),  # filter sub_category by name API
#
#     path('filter/id/<int:pk>/', Sub_CategoryViewSet.as_view({'get': 'filter_sub_category_by_id'}),
#          name='filter_sub_category_by_id'),  # filter sub_category by id API
#
#     # path('filter/date/', Sub_CategoryViewSet.as_view({'get': 'filter_sub_category_by_date'}),
#     # name='filter_category_by_date'),       #  filter category by data API
#
#     path('filter/first-created/', Sub_CategoryViewSet.as_view({'get': 'filter_sub_category_first_created'}),
#          name='filter_sub_category_first_created'),  # filter sub_category first created API
#
#     path('filter/last-created/', Sub_CategoryViewSet.as_view({'get': 'filter_sub_category_last_created'}),
#          name='filter_sub_category_last_created'),  # filter sub_category last created API
#
#     path('filter/lastToFirst-created/', Sub_CategoryViewSet.as_view({'get': 'filter_sub_category_last_to_first_created'}),
#          name='filter_sub_category_last_to_first_created'),  # filter sub_category last to first created API
#
#     path('filter/firstToLast-created/', Sub_CategoryViewSet.as_view({'get': 'filter_sub_category_first_to_last_created'}),
#          name='filter_sub_category_first_to_last_created'),  # filter sub_category last to first created API
#
#     path('search/<str:search_param>', Sub_CategoryViewSet.as_view({'get': 'search_sub_category_by_name'}),
#          name='search_sub_category_by_name'),  # search sub_category by name API
#
#     path('sort/', Sub_CategoryViewSet.as_view({'get': 'sort_sub_categories'}),
#          name='sort_sub_categories'),  # search sub_category by name API
#
# ]
# urlpatterns += router.urls