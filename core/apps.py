from django.apps import AppConfig
import core.signals.users


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):            #Add this line to call the signals.py file and register the handler function
        import core.signals