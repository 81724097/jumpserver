# -*- coding: utf-8 -*-
#

from django.views.generic import ListView, CreateView
from ..models import BulkChangePassword

__all__ = [
    'BulkChangePasswordList', 'BulkChangePasswordCreate',
]


class BulkChangePasswordList(ListView):
    model = BulkChangePassword
    template_name = 'ops/bulk_change_password_list.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'app': _('Bulk change password'),
            'action': _('Bulk change password list')
        }
        kwargs.update(context)
        return super().get_context_data(*args, **kwargs)


class BulkChangePasswordCreate(CreateView):
    model = BulkChangePassword
    template_name = 'ops/bulk_change_password_create.html'
