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
from django.http import HttpResponseRedirect
from django.utils.translation import get_supported_language_variant
from django.conf import settings


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


def change_lang(request):
    lang = request.GET.get('lang', None)
    # print('lang: %s' % lang)
    # print(request.META)
    host = request.get_host()
    # print('host: %s' % host)
    if 'HTTP_REFERER' in request.META:

        refer = request.META['HTTP_REFERER']
        # print('refer: %s' % refer)
        if refer[0:5] == 'https':
            refer_url = refer[8:]
        else:
            refer_url = refer[7:]
        # print('refer url: %s' % refer_url)
        if host != refer_url[:len(host)]:
            refer = '/'
    else:
        refer = '/'
    languages = settings.LANGUAGES
    # print('refer: %s' % refer)

    if lang in [l[0] for l in languages]:
        request.session['_language'] = lang
    return HttpResponseRedirect(refer)
