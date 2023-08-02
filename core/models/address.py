from django.db import models
from core.models.base import *
from core.models.users import *

class Address(BaseModel):
    user = models.ForeignKey(Users, related_name='user_addresses', on_delete=models.CASCADE)
    stat = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zipCode = models.CharField(max_length=20)


    def __str__(self):
        return f"Address ID: {self.id}, City: {self.zipCode}"