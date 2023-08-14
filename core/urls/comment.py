from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.comment import *
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()   # url for class base view
router.register(r'', CommentViewSet, basename='CommentViewSet' )

app_name = 'comment'

urlpatterns = [   # url for function base view
   path('', include(router.urls)),
   # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


   path('Comment-By-product/<int:product_id>/', CommentViewSet.as_view({'get': 'comments_by_product'}), name='comments_by_product'),
   path('Comment-By-user/<int:user_id>/', CommentViewSet.as_view({'get': 'comments_by_user'}), name='comments_by_user'),

]
