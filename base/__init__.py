from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app


# 整合celery 重要，没有这个不成功
__all__ = ['celery_app']
