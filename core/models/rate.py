from django.db import models
from core.models.base import *
from core.models.users import *
from core.models.product import *


class Rate(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_rate')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_rate')
    rate = models.PositiveIntegerField()


    def __str__(self):
        return f"Rate ID: {self.id}, User: {self.user}, Product: {self.product}"
