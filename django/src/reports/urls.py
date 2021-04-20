from django.urls import path
from reports.views import (
    create_report_view,
    render_pdf_view,
    ReportListView,
    ReportDetailView,
)

app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='main'),
    path('save/', create_report_view, name='create-report'),
    path('pdf/<pk>', render_pdf_view, name='pdf'), 
    path('<pk>/', ReportDetailView.as_view(), name='detail'), 
    ]
