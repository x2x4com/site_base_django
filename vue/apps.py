from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class VueConfig(ModuleMixin, AppConfig):
    name = 'vue'
    icon = '<i class="material-icons">settings_applications</i>'
