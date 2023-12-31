from django.db import models
from core.models.users import *
from core.models.product import *
from core.models.base import *

class Comment(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_comment')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name='user_product')
    comment = models.TextField()


    def __str__(self):
        return f"Comment ID: {self.id}, User: {self.user}, Product: {self.product}"