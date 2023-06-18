from django.db import models
from base.models import *
from users.models import *
from product.models import *


class Wish_List(BaseModel):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
