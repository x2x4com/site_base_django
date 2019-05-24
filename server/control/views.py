
from django.utils.translation import ugettext_lazy as _

from material import Layout, Row, Fieldset
from material.frontend.views import ModelViewSet, ListModelView

from django.shortcuts import render
from django.views import generic, static
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView
from django_filters import rest_framework as filters

from . import models
from . import forms
from lib.viewsets import BaseListModelView

# class MyModelViewSet(ModelViewSet):
#    model = models.MyModel


class SomeControlViewSet(ModelViewSet):
    model = models.SomeControl
    # ordering = ['-create_time']
    list_display = ('title', 'type', 'owner', 'create_time', 'tags')
    test_attr = "a"
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title', 'owner', )
    filterset_class = models.SomeControlFilter(queryset=model.objects.all())
    # data_filter = models.SomeControlFilter(queryset=model.objects.all())
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ('title', 'owner', )
    list_view_class = BaseListModelView
    # list_select_related = True

    def get_queryset(self, request, **kwargs):
        # print(kwargs)
        # qs = super(SomeControlViewSet, self).get_queryset(request, **kwargs)
        # print(dir(self))
        return self.model.objects.filter(owner=request.user)

    # def filter_kwargs(self, view_class, **kwargs):
    #     print(view_class)
    #     print(kwargs)
    #     _filter_kwargs = super(SomeControlViewSet, self).filter_kwargs(view_class, **kwargs)
    #     return _filter_kwargs

    # def get_list_view(self):
    #     # print(dir(self))
    #     list_view = super(SomeControlViewSet, self).get_list_view()
    #     # print(list_view)
    #     return list_view


class SomeControlTypeViewSet(ModelViewSet):
    model = models.SomeControlType
    # ordering = ['-create_time']
    list_display = ('name', 'create_time', 'owner')
    # list_select_related = True


class SomeControlTagsViewSet(ModelViewSet):
    model = models.SomeControlTags
    list_display = ('name', 'create_time', 'owner')
    # list_select_related = True
