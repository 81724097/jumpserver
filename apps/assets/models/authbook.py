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
    def get_asset_auth_item(cls, asset, username):
        return cls.objects.filter(asset=asset, username=username).latest()

    @classmethod
    def get_asset_auth(cls, asset, username):
        item = cls.get_asset_auth_item(asset, username)
        if item:
            auth = {
                'password': item.password,
                'private_key': item.private_key,
                'public_key': item.public_key,
            }
        else:
            auth = {
                'password': None,
                'private_key': None,
                'public_key': None,
            }
        return auth

    class Meta:
        get_latest_by = 'date_created'
