#!/usr/bin/env python
# encoding: utf-8
# ===============================================================================
#
#         FILE:
#
#        USAGE:
#
#  DESCRIPTION:
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  YOUR NAME (),
#      COMPANY:
#      VERSION:  1.0
#      CREATED:
#     REVISION:  ---
# ===============================================================================

from material.frontend.views.list import DataTableMixin, ListModelView
from django.views.generic import View
from django_filters.views import FilterMixin
from material.frontend.views import ModelViewSet
from material.frontend import forms
from django.views.generic.base import TemplateResponseMixin


# https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
# todo 页面刷新的时候filter已经生效，datatable刷新也正常
class DFListModelView(ListModelView, FilterMixin):
    datatable_config = {
        'processing': False,
        'serverSide': True,
        'ajax': {
            'url': '.',
        },
        'order': [],
        'ordering': True,
        'orderMulti': True,
        'info': False,
        'bFilter': False,
        'bAutoWidth': True,
        'bLengthChange': False,
        'oLanguage': {
            'oPaginate': {
                'sFirst': "",
                'sLast': "",
                'sNext': "&rang;",
                'sPrevious': "&lang;",
            }
        },
        'responsive': {
            'details': False
        }
    }

    def dispatch(self, request, *args, **kwargs):
        """Handle for browser HTTP and AJAX requests from datatables."""
        self.request_form = forms.DatatableRequestForm(request.GET, prefix='datatable')

        filterset_class = self.get_filterset_class()
        self.filterset = self.get_filterset(filterset_class)

        if not self.filterset.is_bound or self.filterset.is_valid() or not self.get_strict():
            self.object_list = self.filterset.qs
        else:
            self.object_list = self.filterset.queryset.none()

        if 'HTTP_DATATABLE' in request.META:
            handler = self.get_json_data
        elif request.method.lower() in self.http_method_names:
            handler = getattr(
                self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # ajax生成的url要修改一下，现在第二次点击菜单会报错

        _query = request.GET.urlencode()
        print('qs: %s' % _query)

        context = self.get_context_data(filter=self.filterset,
                                        object_list=self.object_list)
        print(context['datatable_config']['ajax']['url'])
        if _query and context['datatable_config']['ajax']['url'] == '.':
            context['datatable_config']['ajax']['url'] += '/?%s' % _query
        else:
            context['datatable_config']['ajax']['url'] = '.'
        # print(context)
        print(context['datatable_config']['ajax']['url'])
        return self.render_to_response(context)


class DFModelViewSet(ModelViewSet):
    def get_list_view_kwargs(self, **kwargs):
        """Configuration arguments for list view.

        May not be called if `get_list_view` is overridden.
        """
        result = {
            'list_display': self.list_display,
            'list_display_links': self.list_display_links,
            'ordering': self.ordering,
            'filterset_fields': self.filterset_fields,
        }
        result.update(kwargs)
        return self.filter_kwargs(self.list_view_class, **result)

    def get_queryset(self, request, **kwargs):
        # print(kwargs)
        # qs = super(SomeControlViewSet, self).get_queryset(request, **kwargs)
        # print(dir(self))
        return self.model.objects.filter(owner=request.user)
