
from django.utils.translation import ugettext_lazy as _

from material import Layout, Row, Fieldset
from material.frontend.views import ModelViewSet, ListModelView

from django.shortcuts import render
from django.views import generic, static
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView

from . import models
from . import forms

# class MyModelViewSet(ModelViewSet):
#    model = models.MyModel


class SomeControlViewSet(ModelViewSet):
    model = models.SomeControl
    # ordering = ['-create_time']
    list_display = ('title', 'type', 'owner', 'create_time', )


class SomeControlTypeViewSet(ModelViewSet):
    model = models.SomeControlType
    # ordering = ['-create_time']
    list_display = ('name',)
    # list_select_related = True



