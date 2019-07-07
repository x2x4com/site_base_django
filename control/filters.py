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
from . import models
from django_filters import rest_framework as rest_framework_filters
import django_filters


# Data Filters
class SomeControlFilter(rest_framework_filters.FilterSet):

    class Meta:
        model = models.SomeControl
        fields = {
            'title': ['iexact'],
            'owner': ['iexact']
        }


# Data Filters
class SomeControlFilter2(django_filters.FilterSet):

    class Meta:
        model = models.SomeControl
        fields = {
            'title': ['iexact'],
            'owner': ['iexact']
        }
