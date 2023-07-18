from django.db import models
from core.models.base import *
from core.models.shopping_cart import *


class Delivery(BaseModel):
    send_with_post= models.IntegerField(default=0)
    send_with_tipax= models.IntegerField(default=0)
    send_with_snapbar= models.IntegerField(default=0)






