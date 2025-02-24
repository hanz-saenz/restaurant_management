from django.urls import path
from .views import *

urlpatterns = [
    path('create/', MenuItemCreateView.as_view(), name='menu-item-create'),
    path('list/', MenuItemListView.as_view(), name='menu-item-list'),
    path('<int:pk>/', MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('update/<int:pk>/', MenuItemUpdateView.as_view(), name='menu-item-update'),
    path('delete/<int:pk>/', MenuItemDeleteView.as_view(), name='menu-item-delete'),
   
]