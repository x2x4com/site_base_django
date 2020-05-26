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

from lib.form import FormCreate, forms


def vv(val):
    print(val)


class DemoForm(FormCreate):
    title = forms.CharField(
        label='标题',
        initial='你好',
        help_text='帮助文字',
        widget=forms.TextInput(attrs={'col': 8}),
        required=True,
        validators=[vv]
    )
    hidden = forms.CharField(
        label='隐藏标题',
        initial='你好',
        help_text='帮助文字',
        widget=forms.TextInput(attrs={'col': 8, 'hidden': True}),
        required=True,
        validators=[vv],
    )
    f1 = forms.DateTimeField(

    )
