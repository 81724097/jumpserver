# -*- coding: utf-8 -*-
#

import uuid

from django.db import models
from django.utils.translation import ugettext as _


class BulkChangePassword(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    hosts = models.ManyToManyField('assets.Asset')
    username = models.CharField(max_length=128, verbose_name=_('User'))
    _password = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Password'))
    _result = models.TextField(blank=True, null=True, verbose_name=_('Result'))
    is_finished = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(null=True)
    date_finished = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

