#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from django.db import models
from django.utils.translation import ugettext as _

from .base import AssetUser
from common.utils import get_logger

logger = get_logger(__file__)


class AuthBook(AssetUser):
    asset = models.ForeignKey(
        'assets.Asset', on_delete=models.CASCADE, verbose_name=_('Asset')
    )

    def __str__(self):
        return '{}@{}'.format(self.username, self.asset)

    @classmethod
    def get_item_latest_by_asset_username(cls, asset, username):
        items = cls.objects.filter(asset=asset, username=username)
        if items:
            item = items.latest()
        else:
            item = None
        return item

    class Meta:
        get_latest_by = 'date_created'
