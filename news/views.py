from django.utils.translation import ugettext_lazy as _

from material import Layout, Row, Fieldset
from material.frontend.views import ModelViewSet

from . import models


# class MyModelViewSet(ModelViewSet):
#    model = models.MyModel

class NewsViewSet(ModelViewSet):
    model = models.News
    # ordering = ['-create_time']
    list_display = ('title', 'type', 'owner', 'create_time')


class TypeViewSet(ModelViewSet):
    model = models.Type
    # ordering = ['-create_time']
    list_display = ('name',)

