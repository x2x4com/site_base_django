
from django.utils.translation import ugettext_lazy as _

from material import Layout, Row, Fieldset

from django.shortcuts import render
from django.views import generic, static
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView
import django_filters

from lib.viewsets import DFListModelView, DFModelViewSet
from . import models
from . import forms


class SomeControlViewSet(DFModelViewSet):
    model = models.SomeControl
    # ordering = ['-create_time']
    list_display = ('title', 'type', 'owner', 'create_time', 'tags')
    list_view_class = DFListModelView
    filterset_fields = ('title', 'type', 'tags')
    list_select_related = True


class SomeControlTypeViewSet(DFModelViewSet):
    model = models.SomeControlType
    # ordering = ['-create_time']
    list_display = ('name', 'create_time', 'owner')
    list_view_class = DFListModelView
    filterset_fields = ('name',)
    list_select_related = True


class SomeControlTagsViewSet(DFModelViewSet):
    model = models.SomeControlTags
    list_display = ('name', 'create_time', 'owner')
    list_view_class = DFListModelView
    filterset_fields = ('name',)
    list_select_related = True
