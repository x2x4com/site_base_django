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
from material.frontend.views.delete import DeleteModelView
from django.views.generic import View
from django_filters.views import FilterMixin
from material.frontend.views import ModelViewSet
from material.frontend import forms
from django.views.generic.base import TemplateResponseMixin
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import Http404
from django.http import HttpResponseRedirect
from django.db.models.deletion import Collector
from django.db import router
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.conf.urls import url
from django.contrib.auth.decorators import login_required


class DFDeleteModelView(DeleteModelView):
    # 重写delete支持多行删除
    def get_object(self,):
        """Retrieve the object for delete.

        Check object delete permission at the same time.
        """
        # print('in get_object')
        queryset = self.get_queryset()
        if hasattr(self, 'ids'):
            if len(self.ids) > 0:
                # in Blog.objects.filter(pk__in=[1, 4, 7])
                self.queryset = queryset.model.objects.filter(id__in=self.ids)
                return self.queryset.all()
        model = queryset.model
        # print(self.pk_url_kwarg)
        pk = self.kwargs.get(self.pk_url_kwarg)
        # print('delete pk: %s' % pk)
        if pk is not None:
            try:
                # print("get_object 1")
                self.kwargs[self.pk_url_kwarg] = model._meta.pk.to_python(pk)
            except (ValidationError, ValueError):
                raise Http404
        # print("get_object 2")
        obj = super(DeleteModelView, self).get_object()
        if not self.has_object_permission(self.request, obj):
            raise PermissionDenied
        # print("get_object 3")
        return obj

    def _get_deleted_objects(self):
        collector = Collector(using=router.db_for_write(self.object))
        obj = [self.object]
        if hasattr(self, 'ids'):
            obj = list()
            if hasattr(self, 'objects'):
                for _obj in self.objects:
                    obj.append(_obj)
        collector.collect(obj)
        return collector.data

    def delete(self, request, *args, **kwargs):
        # response = super(DeleteModelView, self).delete(request, *args, **kwargs)
        # print("delete 0")
        self.ids = request.POST.getlist('pk', default=None)
        # print('ids: %s' % self.ids)
        _confirm = request.POST.get('_confirm', None)
        # print(_confirm)
        if len(self.ids) > 0:
            self.objects = self.get_object()
            self.object = self.objects[0]
            # print(self.object)
        else:
            self.object = self.get_object()
            # print(self.object)

        if _confirm is None and len(self.ids) > 0:
            self.template_name = 'material/frontend/views/muti_confirm_delete.html'
            # print(self.get_template_names())
            context = self.get_context_data(object=self.object)
            # print(context)
            return self.render_to_response(context)

        # print("delete 1")
        success_url = self.get_success_url()
        # print("delete 2")
        if len(self.ids) > 0:
            # print("删除多条")
            for _obj in self.objects:
                _obj.delete()
        else:
            # print("删除单条")
            self.object.delete()
        # print("delete 3")
        self.message_user()
        return HttpResponseRedirect(success_url)

    def message_user(self):
        if hasattr(self, 'objects'):
            link = ""
            for _obj in self.objects:
                if len(link) == 0:
                    link = force_text(_obj)
                else:
                    link = link + " , " + force_text(_obj)
        else:
            link = force_text(self.object)

        message = _('The {name} "{link}"  was deleted successfully.'.format(
            name=force_text(self.model._meta.verbose_name),
            link=link
        ))
        messages.add_message(self.request, messages.SUCCESS, message, fail_silently=True)

    def post(self, request, *args, **kwargs):
        print("in post")
        print(request.path)

        return self.delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print('in get')
        _path = request.path.lstrip('/').rstrip('/').split('/')
        # print(_path)
        _target = '/'.join(_path[0:-2])
        # print(_target)
        try:
            int(_path[3])
        except ValueError:
            return HttpResponseRedirect('/' + _target)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print(context)
        print(self.get_template_names())
        return self.render_to_response(context)


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
        },
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
        # print('qs: %s' % _query)

        context = self.get_context_data(filter=self.filterset,
                                        object_list=self.object_list)
        # print(context['datatable_config']['ajax']['url'])
        if _query:
            context['datatable_config']['ajax']['url'] = request.path + '?%s' % _query
        else:
            context['datatable_config']['ajax']['url'] = request.path
        # print(context)
        # print(context['datatable_config']['ajax']['url'])
        return self.render_to_response(context)

    def get_columns_def(self):
        """Return columns definition for the datables js config."""
        columns = list()

        for field_name in self.get_list_display():
            if field_name == 'pk':
                columns.append({"targets": 0, "data": "pk", "orderable": False, "checkboxes": {"selectRow": True}})
            else:
                columns.append({'data': field_name, 'orderable': self.get_data_attr(field_name).orderable})

        return columns

    def get_list_display(self):
        """Return list of columns to display."""
        # print(dir(self.viewset))
        if hasattr(self, 'viewset'):
            if hasattr(self.viewset, 'list_actions'):
                return ('pk', ) + self.list_display
        return self.list_display

    def get_list_display_links(self, list_display):
        """Return columns list that would be linked to the object details.

        If `self.list_display_links` is not set, the first column would be used.
        """
        if (self.list_display_links or
                self.list_display_links is None or
                not list_display):
            return self.list_display_links
        else:
            # Use only the first item in list_display as link
            if hasattr(self, 'viewset'):
                if hasattr(self.viewset, 'list_actions'):
                    return list(list_display)[1:2]
            return list(list_display)[:1]


class DFModelViewSet(ModelViewSet):
    # filterset_fields = ( )
    list_view_class = DFListModelView
    delete_view_class = DFDeleteModelView
    login_require = True

    @property
    def urls(self):
        """Collect url specs from the instance attributes.

        Assumes that each attribute with name ending with `_view`
        contains triple (regexp, view, url_name)
        """
        result = []

        format_kwargs = {
            'model_name': self.model._meta.model_name
        }

        url_entries = (
            getattr(self, attr)
            for attr in dir(self)
            if attr.endswith('_view')
            if isinstance(getattr(self, attr), (list, tuple))
        )
        for url_entry in url_entries:
            regexp, view, name = url_entry
            if hasattr(self, 'login_require') and self.login_require is True:
                result.append(
                    url(regexp.format(**format_kwargs),
                        login_required(view),
                        name=name.format(**format_kwargs))
                )
            else:
                result.append(
                    url(regexp.format(**format_kwargs),
                        view,
                        name=name.format(**format_kwargs))
                )

        return result

    def get_list_view_kwargs(self, **kwargs):
        """Configuration arguments for list view.

        May not be called if `get_list_view` is overridden.
        """
        result = {
            'list_display': self.list_display,
            'list_display_links': self.list_display_links,
            'ordering': self.ordering,
        }

        if hasattr(self, 'list_actions'):
            result.update({'list_actions': self.list_actions})

        if hasattr(self, 'filterset_fields'):
            result.update({'filterset_fields': self.filterset_fields})
        else:
            result.update({'filterset_fields': ()})

        if hasattr(self, 'filterset_class'):
            result.update({'filterset_class': self.filterset_class})
        else:
            result.update({'filterset_class': ()})

        result.update(kwargs)
        return self.filter_kwargs(self.list_view_class, **result)

    # def get_queryset(self, request, **kwargs):
    #     # print(kwargs)
    #     # qs = super(SomeControlViewSet, self).get_queryset(request, **kwargs)
    #     # print(dir(self))
    #     return self.model.objects.filter(owner=request.user)
