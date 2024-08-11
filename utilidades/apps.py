from django.apps import AppConfig


class UtilidadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utilidades'
    
    def ready(self):
        import utilidades.signals
