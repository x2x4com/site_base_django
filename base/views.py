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
from . import forms
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils.translation import get_supported_language_variant
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import auth


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


@login_required
def change_pwd(request):
    context = {
        'success': False,
        'dis_msg': False,
        'msg': '',
        'form': forms.ChangePWDForm()
    }
    if request.method == 'POST':
        form = forms.ChangePWDForm(request.POST)
        if form.is_valid():
            username = request.user.username
            old_password = form.cleaned_data['old_password']
            user = auth.authenticate(username=username, password=old_password)
            # print(user)
            if user is not None and user.is_active:
                new_password1 = form.cleaned_data['new_password1']
                user.set_password(new_password1)
                user.save()
                context['success'] = True
                msg = '密码修改成功'
            else:
                msg = '用户不存在或未激活或密码错误'
        else:
            msg = '表单验证错误，请检查'
        context['msg'] = msg
        context['dis_msg'] = True
        context['form'] = form
        # print(context)

    return render(request, 'material/frontend/base_forms.html', context)
