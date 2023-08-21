from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from core.views.users import *


app_name = "Users"

urlpatterns = [
    path('create/', UserRegistrationView.as_view(), name='user-register'),
    path('', UserListView.as_view(), name='user-list'),
    path('update/', UserProfileUpdateView.as_view(), name='user-profile-update'),
    path('change_password/', UserChangePasswordView.as_view(), name='change_password'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('promote-to-admin/<int:user_id>/', PromoteToAdminView.as_view(), name='promote-to-admin'),

]