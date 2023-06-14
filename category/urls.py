from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .import views


router = routers.DefaultRouter()        # url for class base view
router.register('category_view_set',views.CategoryViewSet),

app_name = "category"
urlpatterns = [       # url for function base view

]
urlpatterns += router.urls