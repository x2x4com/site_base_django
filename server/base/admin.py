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

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Site admin')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site admin')


admin_site = MyAdminSite()

