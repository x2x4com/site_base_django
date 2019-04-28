from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# class MyModel(models.Model):
#     name = models.CharField(max_length=250)


class News(models.Model):
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    title = models.CharField(_('title'), max_length=300)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ['create_time']

