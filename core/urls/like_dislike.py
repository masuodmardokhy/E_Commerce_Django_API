from django.urls import path
from core.views.like_dislike import like_product, dislike_product

urlpatterns = [
    path('like/', like_product, name='like_product'),
    path('dislike/', dislike_product, name='dislike_product'),
]