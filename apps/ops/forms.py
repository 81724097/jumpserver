# -*- coding: utf-8 -*-
#
from django import forms
from django.utils.translation import ugettext as _

from assets.models import SystemUser, Asset
from .models import CommandExecution, BulkChangePassword


class CommandExecutionForm(forms.ModelForm):
    class Meta:
        model = CommandExecution
        fields = ['run_as', 'command']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        run_as_field = self.fields.get('run_as')
        run_as_field.queryset = SystemUser.objects.all()


class BulkChangePasswordForm(forms.ModelForm):
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput,
        max_length=128, strip=False, required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        hosts_field = self.fields.get('hosts')
        hosts_field.queryset = Asset.objects.all()

    class Meta:
        model = BulkChangePassword
        fields = [
            'name', 'username', 'hosts', 'password'
        ]
        widgets = {
            'hosts': forms.SelectMultiple(
                attrs={'class': 'select2', 'data-placeholder': _("Asset")}
            ),
        }

    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        ch_password = super().save(commit=commit)
        if password:
            ch_password.password = password
            ch_password.save()
        return ch_password
