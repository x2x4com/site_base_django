from django.utils.translation import ugettext_lazy as _

from material import Layout, Row, Fieldset

from django.shortcuts import render
from django.views import generic, static
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView
import django_filters

from lib.viewsets import DFModelViewSet
from . import models
from . import forms


class SomeControlViewSet(DFModelViewSet):
    model = models.SomeControl
    # ordering = ['-create_time']
    list_display = ('pk', 'title', 'type', 'owner', 'create_time', 'show_tags')
    list_display_links = ('title', )
    filterset_fields = ('title', 'type', 'tags')
    list_select_related = True
    list_actions = ('Delete selected objects', 'action/delete/')

    def show_tags(self, obj):
        tags = obj.tags.all()
        tags = [t.name for t in tags]
        return ", ".join(tags)

    def _pk(self, obj):
        # print(dir(obj.pk))
        return int(obj.pk)


class SomeControlTypeViewSet(DFModelViewSet):
    model = models.SomeControlType
    # ordering = ['-create_time']
    list_display = ('name', 'create_time', 'owner')
    # list_view_class = DFListModelView
    # filterset_fields = ('name',)
    list_select_related = True


class SomeControlTagsViewSet(DFModelViewSet):
    model = models.SomeControlTags
    list_display = ('name', 'create_time', 'owner')
    filterset_fields = ('name',)
    list_select_related = True
