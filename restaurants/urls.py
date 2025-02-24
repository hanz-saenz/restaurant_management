from django.urls import path
from .views import *

urlpatterns = [
    path('list/', RestaurantListView.as_view(), name='restaurant-detail'),
    path('create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('update/<int:pk>/', RestaurantUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', RestaurantDeleteView.as_view(), name='user-delete'),
]