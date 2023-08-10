from django.db import models
from django.contrib.auth.models import User

class UserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    is_like = models.BooleanField(default=False)
    is_dislike = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)