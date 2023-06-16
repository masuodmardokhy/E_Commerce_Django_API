from django.db import models
from base.models import *


class Wish_List(BaseModel):
    name = models.CharField(max_length=30)
