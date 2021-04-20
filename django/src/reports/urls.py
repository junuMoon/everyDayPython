from django.urls import path
from reports.views import create_report_view

app_name = 'reports'

urlpatterns = [path('save', create_report_view, name='create-report')]
