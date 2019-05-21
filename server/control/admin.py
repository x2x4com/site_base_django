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

from django import forms
from django.contrib import admin
from django.db import models as django
from django.utils.text import Truncator
from django.utils.html import mark_safe, format_html
from django.utils.translation import ugettext_lazy as _

from . import models


@admin.register(models.SomeControl)
class SomeControlAdmin(admin.ModelAdmin):
    icon = '<i class="fa fa-tint"></i>'
    list_display = ('title', 'type', 'owner', 'create_time', )


@admin.register(models.SomeControlType)
class SomeControlTypeAdmin(admin.ModelAdmin):
    icon = '<i class="fa fa-tint"></i>'
    actions = None
    list_display = ('name',)
