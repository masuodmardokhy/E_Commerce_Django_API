from django.db import models
from core.models.base import *
from core.models.order import *


class Delivery(BaseModel):
    name = models.CharField(max_length=20)
    send_price = models.IntegerField(default=0)






