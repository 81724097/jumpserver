# -*- coding: utf-8 -*-
#

from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from ..models import BulkChangePassword
from ..forms import BulkChangePasswordForm

__all__ = [
    'BulkChangePasswordList', 'BulkChangePasswordCreate',
    'BulkChangePasswordDetail'
]


class BulkChangePasswordList(ListView):
    model = BulkChangePassword
    template_name = 'ops/bulk_change_password_list.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'app': _('批量改密'),
            'action': _('批量改密任务列表')
        }
        kwargs.update(context)
        return super().get_context_data(*args, **kwargs)


class BulkChangePasswordCreate(CreateView):
    model = BulkChangePassword
    form_class = BulkChangePasswordForm
    template_name = 'ops/bulk_change_password_create_or_update.html'
    success_url = reverse_lazy('ops:bulk-change-password-list')

    def get_context_data(self, *args, **kwargs):
        context = {
            'app': _('批量改密'),
            'action': _('创建批量改密任务')
        }
        kwargs.update(context)
        return super().get_context_data(*args, **kwargs)


class BulkChangePasswordDetail(DetailView):
    model = BulkChangePassword
    template_name = 'ops/bulk_change_password_detail.html'
