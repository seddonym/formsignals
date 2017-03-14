from django.apps import AppConfig as BaseAppConfig


default_app_config = 'formsignals.priority.AppConfig'


class AppConfig(BaseAppConfig):
    name = 'formsignals.priority'

    def ready(self):
        # Imports the receivers file
        from . import receivers  # NOQA
