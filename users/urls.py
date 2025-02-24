from .views import UploadUsersView
from django.urls import path
from .views import *

urlpatterns = [
    path('upload-users/', UploadUsersView.as_view(), name='upload-users'),
    path('list/', UserListView.as_view(), name='restaurant-detail'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]