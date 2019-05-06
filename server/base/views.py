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

from django.shortcuts import render
# from . import forms
from django.http import Http404


def index_view(request):
    # context = {
    #     'login': forms.LoginForm(),
    #     'registration': forms.RegistrationForm(),
    #     'checkout': forms.CheckoutForm(),
    #     'order': forms.OrderForm(),
    #     'comment': forms.CommentForm(),
    #     'bank': forms.BankForm(),
    # }
    # return render(request, 'index.html', context)
    raise Http404('Page not find')
