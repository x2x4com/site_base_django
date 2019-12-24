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
from django import forms
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


class ChangePWDForm(forms.Form):
    old_password = forms.CharField(
        required=True,
        label="原密码",
        error_messages={'required':  '请输入原密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "原密码",
            }
        ),
    )
    new_password1 = forms.CharField(
        required=True,
        label="新密码",
        error_messages={'required': '请输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "新密码",
            }
        ),
    )
    new_password2 = forms.CharField(
        required=True,
        label="确认密码",
        error_messages={'required': '请再次输入新密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "确认密码",
            }
        ),
     )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("所有项都为必填项")
        elif self.cleaned_data['new_password1'] != self.cleaned_data['new_password2']:
            raise forms.ValidationError("两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangePWDForm, self).clean()
        return cleaned_data
