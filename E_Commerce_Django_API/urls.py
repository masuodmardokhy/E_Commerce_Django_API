"""
URL configuration for E_Commerce_Django_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_spectacular import openapi
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view

# from core import admin
from core.admin import *
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView,SpectacularRedocView




urlpatterns = [

    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name= "schema"),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('category/', include('core.urls.category')),
    path('cart_item/', include('core.urls.cart_item')),
    path('delivery/', include('core.urls.delivery')),
    path('order/', include('core.urls.order')),
    path('product/', include('core.urls.product')),
    path('shopping_cart/', include('core.urls.shopping_cart')),
    path('users/', include('core.urls.users')),
    path('wish_list/', include('core.urls.wish_list')),
    path('rate/', include('core.urls.rate')),
    path('address/', include('core.urls.address')),
    path('comment/', include('core.urls.comment')),
    path('feedback/', include('core.urls.like_dislike')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-token-auth/', views.obtain_auth_token) ,
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
