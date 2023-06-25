from django.apps import AppConfig
from core.signals.product import *


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'


    def ready(self):
        import product.signals
