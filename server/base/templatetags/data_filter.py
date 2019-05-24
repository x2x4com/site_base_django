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

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def gen_filter_form(context, filter):
    request = context['request']
    model = filter.queryset
    filter.queryset = model.filter(owner=request.user)
    filter.request = request
    return filter
