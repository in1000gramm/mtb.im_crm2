from django.apps import AppConfig


class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'
    verbose_name = "База клиентов" # А здесь, имя которое необходимо отобразить в админке