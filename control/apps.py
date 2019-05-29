from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class ControlConfig(ModuleMixin, AppConfig):
    name = 'control'
    icon = '<i class="material-icons">assessment</i>'

    def has_perm(self, user):
        return user.is_superuser
