from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# Create your models here.
User = get_user_model()


class SomeControlType(models.Model):
    name = models.CharField(_('type'), max_length=100)

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('type')

    def __str__(self):
        return self.name


class SomeControl(models.Model):
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    title = models.CharField(_('title'), max_length=300)
    body = models.TextField(_('text'))
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=_('owner'), null=True)
    type = models.ForeignKey(SomeControlType, on_delete=models.SET_NULL, verbose_name=_('type'), null=True)

    class Meta:
        verbose_name = _('control1')
        verbose_name_plural = _('control')
        ordering = ['-create_time']

    def __str__(self):
        return self.title

