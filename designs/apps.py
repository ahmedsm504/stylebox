# designs/apps.py
from django.apps import AppConfig

class DesignsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'designs'

    def ready(self):
        import designs.signals  # 👈 مهم عشان يشتغل
