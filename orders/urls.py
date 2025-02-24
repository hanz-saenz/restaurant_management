from django.urls import path
from .views import *

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order-create'),
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),

    path('restaurants/<int:restaurant_id>/generate-sales-report/', GenerateSalesReportView.as_view(), name='generate-sales-report'),
    path('tasks/<str:task_id>/status/', CheckReportStatusView.as_view(), name='check-report-status'),
    path('reports/download/<str:filename>/', DownloadReportView.as_view(), name='download-report'),
]