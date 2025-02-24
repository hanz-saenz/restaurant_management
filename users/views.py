from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny

import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .tasks import process_user_upload
from .models import User
from .serializers import *
from rest_framework import generics, permissions
from menu.pagination import CustomPageNumberPagination
from .filters import UserFilter 
import django_filters

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]


class UploadUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "File is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar el límite de 20 usuarios
        df = pd.read_csv(file)
        if len(df) > 20:
            return Response({"error": "Maximum 20 users allowed"}, status=status.HTTP_400_BAD_REQUEST)

        # Iniciar la tarea Celery
        task = process_user_upload.delay(file.read().decode('utf-8'))
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
    


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]  # Habilita el filtrado
    filterset_class = UserFilter

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny] 


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]



class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  