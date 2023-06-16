from django.db import models
from django.utils.timezone import datetime



class BaseModel(models.Model):
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
