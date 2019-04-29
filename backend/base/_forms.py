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
import django
from django.forms import *  # NOQA
from material.base import LayoutMixin as ViewformLayoutMixin


class SourceCodeMixin(object):
    def source(self):
        import inspect
        import itertools

        lines = inspect.getsourcelines(self.__class__)[0]
        lines = [x for x in itertools.takewhile(lambda x: not x.strip().startswith('template'), lines)]
        return ''.join(lines)


class Form(SourceCodeMixin, django.forms.Form):
    pass


class LayoutMixin(SourceCodeMixin, ViewformLayoutMixin):
    pass
