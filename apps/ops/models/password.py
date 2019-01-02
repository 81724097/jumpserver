# -*- coding: utf-8 -*-
#

import uuid
import json

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class BulkChangePassword(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    username = models.CharField(max_length=128, verbose_name=_('User'))
    hosts = models.ManyToManyField('assets.Asset', verbose_name=_('Asset'))
    _password = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('Password'))
    _result = models.TextField(blank=True, null=True, verbose_name=_('Result'))
    is_finished = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(null=True)
    date_finished = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    @property
    def result(self):
        if self._result:
            return json.loads(self._result)
        else:
            return {}

    @result.setter
    def result(self, item):
        self._result = json.dumps(item)

    @property
    def hosts_count(self):
        return self.hosts.count()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password_raw):
        self._password = password_raw
