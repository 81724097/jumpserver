# -*- coding: utf-8 -*-
#


from rest_framework import viewsets
from rest_framework.views import APIView, Response
from common.permissions import IsOrgAdmin
from common.utils import get_object_or_none
from assets.tasks import change_password_bulk
from ..serializers import BulkChangePasswordSerializer
from ..models import BulkChangePassword


class BulkChangePasswordViewSet(viewsets.ModelViewSet):
    serializer_class = BulkChangePasswordSerializer
    permission_classes = (IsOrgAdmin,)
    queryset = BulkChangePassword.objects.all()


class BulkChangePasswordRunApi(APIView):
    permission_classes = (IsOrgAdmin,)

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        ch_password = get_object_or_none(BulkChangePassword, id=pk)

        username = ch_password.username
        password = ch_password.password
        assets = ch_password.hosts.all()

        task = change_password_bulk.delay(
            username=username, password=password, assets=assets
        )
        from celery.result import AsyncResult

        return Response({'task': task.id})
