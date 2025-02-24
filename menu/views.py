from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import MenuItem
from .serializers import MenuItemSerializer
from .pagination import CustomPageNumberPagination
from .filters import MenuItemFilter 
import django_filters

# Crear un nuevo ítem del menú
class MenuItemCreateView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden crear ítems
    

# Listar todos los ítems del menú
class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden ver la lista
    pagination_class = CustomPageNumberPagination 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]  # Habilita el filtrado
    filterset_class = MenuItemFilter

# Obtener los detalles de un ítem del menú específico
class MenuItemDetailView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles

# Actualizar un ítem del menú existente
class MenuItemUpdateView(generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden actualizar

# Eliminar un ítem del menú
class MenuItemDeleteView(generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden eliminar