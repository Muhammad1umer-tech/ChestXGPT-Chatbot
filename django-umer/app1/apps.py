"""
app.py
"""
from django.apps import AppConfig
class App1Config(AppConfig):
    """
    Configuration class for the app1 application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1'

    def ready(self):
        """
        Method called when the application is ready.
        """
        import app1.signals
