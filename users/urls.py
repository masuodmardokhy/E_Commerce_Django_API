from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .import views


router = routers.DefaultRouter()        # url for class base view
router.register('user_view_set', views.UserViewSet, basename= 'user_view_set' ),

app_name = "users"
urlpatterns = [       # url for function base view
   path('', include(router.urls)),
]
urlpatterns += router.urls