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


from django.contrib.auth.models import Permission
from django.core.validators import MaxLengthValidator
from django.core.files import File
from django.forms.widgets import SelectDateWidget
from django.template import Template
from django.utils import timezone
# import django
import django.forms as forms
from material.base import LayoutMixin as ViewformLayoutMixin


class SourceCodeMixin(object):
    def source(self):
        import inspect
        import itertools

        lines = inspect.getsourcelines(self.__class__)[0]
        lines = [x for x in itertools.takewhile(lambda x: not x.strip().startswith('template'), lines)]
        return ''.join(lines)


class Form(SourceCodeMixin, forms.Form):
    pass


class LayoutMixin(SourceCodeMixin, ViewformLayoutMixin):
    pass


class WizardForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()


class WizardForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class SelectDateWidgetForm(Form):
    description = "SelectDateWidget options"

    field1 = forms.DateField(
        help_text='default', widget=SelectDateWidget)
    field2 = forms.DateField(
        help_text='initial value', widget=SelectDateWidget, initial=timezone.now)
    field3 = forms.DateField(
        help_text='custom empty label', widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day")))
    field4 = forms.DateField(
        help_text='disabled', widget=SelectDateWidget, initial=timezone.now, disabled=True, required=False)
