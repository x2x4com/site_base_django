#!/usr/bin/env python3
# encoding: utf-8
# ===============================================================================
#
#         FILE:  start
#
#        USAGE:  ./start
#
#  DESCRIPTION:  blockscanner
#
#      OPTIONS:  ---
# REQUIREMENTS:  ---
#         BUGS:  ---
#        NOTES:  ---
#       AUTHOR:  x2x4(x2x4@qq.com)
#      COMPANY:  x2x4
#      VERSION:  1.0
#      CREATED:  2018/08/06 22:25
#     REVISION:  ---
# ===============================================================================
from __future__ import absolute_import
from celery import Celery
from celery.signals import after_setup_logger
from kombu import Exchange, Queue
import os
import logging
import sys
from django.conf import settings


project = 'base'
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % project)


app = Celery(project)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


if __name__ == '__main__':
    app.start()
