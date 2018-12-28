# -*- coding: utf-8 -*-
#


from rest_framework import viewsets
from rest_framework.views import APIView, Response
from common.permissions import IsOrgAdmin
from ..serializers import BulkChangePasswordSerializer
from ..models import BulkChangePassword
from ..tasks import run_bulk_change_password


class BulkChangePasswordViewSet(viewsets.ModelViewSet):
    serializer_class = BulkChangePasswordSerializer
    permission_classes = (IsOrgAdmin,)
    queryset = BulkChangePassword.objects.all()


class BulkChangePasswordRunApi(APIView):
    permission_classes = (IsOrgAdmin,)

    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        task = run_bulk_change_password.delay(pk)
        return Response({'task': task.id})
