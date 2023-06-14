from django.db import models


class Delivery(models.Model):
    send = models.BooleanField(default=False)
    products_price = models.PositiveIntegerField()
    send_price = models.PositiveIntegerField()
    send_price_and_total_price = models.PositiveIntegerField()


    def total_price(self):
        if self.send is True:
            self.send_price_and_total_price = (self.products_price + self.send_price)
            return int (self.send_price_and_total_price)
        else:
            return self.products_price




