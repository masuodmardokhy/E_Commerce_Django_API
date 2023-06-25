from django.apps import AppConfig
from core.signals.category import *

class CategoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category'


    def ready(self):
        import category.signals
