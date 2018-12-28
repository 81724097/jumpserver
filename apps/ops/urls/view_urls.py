# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals
from django.urls import path

from .. import views

__all__ = ["urlpatterns"]

app_name = "ops"

urlpatterns = [
    # Resource Task url
    path('task/', views.TaskListView.as_view(), name='task-list'),
    path('task/<uuid:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<uuid:pk>/adhoc/', views.TaskAdhocView.as_view(), name='task-adhoc'),
    path('task/<uuid:pk>/history/', views.TaskHistoryView.as_view(), name='task-history'),
    path('adhoc/<uuid:pk>/', views.AdHocDetailView.as_view(), name='adhoc-detail'),
    path('adhoc/<uuid:pk>/history/', views.AdHocHistoryView.as_view(), name='adhoc-history'),
    path('adhoc/history/<uuid:pk>/', views.AdHocHistoryDetailView.as_view(), name='adhoc-history-detail'),
    path('celery/task/<uuid:pk>/log/', views.CeleryTaskLogView.as_view(), name='celery-task-log'),

    path('command-execution/', views.CommandExecutionListView.as_view(), name='command-execution-list'),
    path('command-execution/start/', views.CommandExecutionStartView.as_view(), name='command-execution-start'),

    path('bulk-change-password/', views.BulkChangePasswordList.as_view(), name='bulk-change-password-list'),
    path('bulk-change-password/create/', views.BulkChangePasswordCreate.as_view(), name='bulk-change-password-create'),
    path('bulk-change-password/<uuid:pk>/', views.BulkChangePasswordDetail.as_view(), name='bulk-change-password-detail'),
]
