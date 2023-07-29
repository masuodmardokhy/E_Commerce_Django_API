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
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
# from core import admin
from core.admin import *




urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('core.urls.category')),
    path('cart_item/', include('core.urls.cart_item')),
    path('delivery/', include('core.urls.delivery')),
    path('order/', include('core.urls.order')),
    path('product/', include('core.urls.product')),
    path('shopping_cart/', include('core.urls.shopping_cart')),
    # path('sub_category/', include('core.urls.sub_category')),
    path('users/', include('core.urls.users')),
    path('wish_list/', include('core.urls.wish_list')),
    path('rate/', include('core.urls.rate')),
    path('address/', include('core.urls.address')),
    path('comment/', include('core.urls.comment')),

    path('api-token-auth/', views.obtain_auth_token) ,
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
