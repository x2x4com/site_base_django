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


class DFDeleteModelView(DeleteModelView):
    # 重写delete支持多行删除
    def get_object(self, _ids=None):
        """Retrieve the object for delete.

        Check object delete permission at the same time.
        """
        print('in get_object')
        queryset = self.get_queryset()
        if _ids is None:

            model = queryset.model
            print(self.pk_url_kwarg)
            pk = self.kwargs.get(self.pk_url_kwarg)
            print('delete pk: %s' % pk)
            if pk is not None:
                try:
                    print("get_object 1")
                    self.kwargs[self.pk_url_kwarg] = model._meta.pk.to_python(pk)
                except (ValidationError, ValueError):
                    raise Http404
            print("get_object 2")
            obj = super(DeleteModelView, self).get_object()
            if not self.has_object_permission(self.request, obj):
                raise PermissionDenied
            print("get_object 3")
            return obj
        # in Blog.objects.filter(pk__in=[1, 4, 7])
        self.queryset = queryset.model.objects.filter(id__in=_ids)
        return self.queryset.all()

    def delete(self, request, *args, **kwargs):
        # response = super(DeleteModelView, self).delete(request, *args, **kwargs)
        print("delete 0")
        ids = request.POST.getlist('pk', default=None)
        print(ids)
        _confirm = request.POST.get('_confirm', None)
        print(_confirm)
        self.object = self.get_object(_ids=ids)
        if _confirm is None:
            context = dict()
            for _obj in self.object:
                print(dir(_obj))
                print(type(_obj))
                context.update(self.get_context_data(object=_obj))
            return self.render_to_response(context)
        print("delete 1")
        success_url = self.get_success_url()
        print("delete 2")
        self.object.delete()
        print("delete 3")
        self.message_user()
        return HttpResponseRedirect(success_url)

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
        print(context['datatable_config']['ajax']['url'])
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


class DFModelViewSet(ModelViewSet):
    # filterset_fields = ( )
    list_view_class = DFListModelView
    delete_view_class = DFDeleteModelView

    def get_list_view_kwargs(self, **kwargs):
        """Configuration arguments for list view.

        May not be called if `get_list_view` is overridden.
        """
        result = {
            'list_display': self.list_display,
            'list_display_links': self.list_display_links,
            'ordering': self.ordering,
        }

        if hasattr(self, 'filterset_fields'):
            result.update({'filterset_fields': self.filterset_fields})

        result.update(kwargs)
        return self.filter_kwargs(self.list_view_class, **result)

    def get_queryset(self, request, **kwargs):
        # print(kwargs)
        # qs = super(SomeControlViewSet, self).get_queryset(request, **kwargs)
        # print(dir(self))
        return self.model.objects.filter(owner=request.user)
