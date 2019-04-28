from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class NewsConfig(ModuleMixin, AppConfig):
    name = 'news'
    icon = '<i class="material-icons">settings_applications</i>'
