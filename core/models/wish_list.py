from django.db import models
from core.models.base import *
from core.models.users import *
from core.models.product import *


class Wish_List(BaseModel):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
