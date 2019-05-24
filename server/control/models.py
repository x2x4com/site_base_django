from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as filters


# Create your models here.
User = get_user_model()


class SomeControlType(models.Model):
    name = models.CharField(_('type'), max_length=100)
    owner = models.ForeignKey(User, related_name='type_owner', on_delete=models.SET_NULL, verbose_name=_('owner'), null=True)
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('type')

    def __str__(self):
        return self.name


class SomeControl(models.Model):
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    title = models.CharField(_('title'), max_length=300)
    body = models.TextField(_('text'))
    owner = models.ForeignKey(User, related_name='control_owner', on_delete=models.SET_NULL, verbose_name=_('owner'), null=True)
    type = models.ForeignKey(SomeControlType, related_name='control_type', on_delete=models.SET_NULL, verbose_name=_('type'), null=True)
    tags = models.ManyToManyField('SomeControlTags', related_name='control_tags')

    class Meta:
        verbose_name = _('control')
        verbose_name_plural = _('control')
        ordering = ['-create_time']

    def __str__(self):
        return self.title


class SomeControlTags(models.Model):
    name = models.CharField(_('name'), max_length=300)
    create_time = models.DateTimeField(_('create_time'), auto_now_add=True)
    owner = models.ForeignKey(User, related_name='tags_owner', on_delete=models.SET_NULL, verbose_name=_('owner'), null=True)

    class Meta:
        verbose_name = _('tags')
        ordering = ['-create_time', 'owner']

    def __str__(self):
        return self.name


# Data Filters
class SomeControlFilter(filters.FilterSet):

    class Meta:
        models = SomeControl
        fields = {
            'title': ['iexact'],
            'owner': ['iexact']
        }

