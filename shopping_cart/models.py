from django.db import models


class Shopping_Cart(models.Model):
    total_price = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return self.total_price
