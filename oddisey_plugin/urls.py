"""
URLs for oddisey_plugin.
"""
from django.urls import path
from .views import AppInfoView

urlpatterns = [
    path('info', AppInfoView.as_view(), name='oddisey-info'),
]
