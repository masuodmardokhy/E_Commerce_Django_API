from django.db import models
from core.models.users import Users
from core.models.product import *
from core.models.comment import *



class Like_Dislike(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE,  null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    is_like = models.BooleanField(default=False)
    is_dislike = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)