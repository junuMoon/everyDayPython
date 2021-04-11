from django.urls import path
from sales.views import (
    home_view,
    SaleListView,
    # SaleDetailView,
    sale_detail_view
)

app_name = 'sales'

urlpatterns = [
    path(route='', view=home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='list'),
    # path('sales/<pk>/', SaleDetailView.as_view(), name='detail')
    path('sales/<pk>/', sale_detail_view, name='detail')
]
