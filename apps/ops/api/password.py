# -*- coding: utf-8 -*-
#


from rest_framework import viewsets
from common.permissions import IsOrgAdmin
from ..serializers import BulkChangePasswordSerializer
from ..models import BulkChangePassword


class BulkChangePasswordViewSet(viewsets.ModelViewSet):
    serializer_class = BulkChangePasswordSerializer
    permission_classes = (IsOrgAdmin,)
    queryset = BulkChangePassword.objects.all()
