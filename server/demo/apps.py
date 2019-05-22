from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class DemoConfig(ModuleMixin, AppConfig):
    name = 'demo'
    icon = '<i class="material-icons">cake</i>'
