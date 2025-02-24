from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from .tasks import generate_sales_report
from restaurants.models import Restaurant
from rest_framework.permissions import IsAuthenticated
from .tasks import generate_sales_report

from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer

import os
from django.http import FileResponse, HttpResponseNotFound


# Crear una nueva orden
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden crear órdenes

# Listar todas las órdenes
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden ver la lista

# Obtener los detalles de una orden específica
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden ver los detalles

# Actualizar una orden existente
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden actualizar

# Eliminar una orden
class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden eliminar

class GenerateSalesReportView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, restaurant_id):
        status = request.data.get('status')
        if not status:
            return Response({"error": "status is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({"error": "Restaurant not found"}, status=status.HTTP_404_NOT_FOUND)

        # Iniciar la tarea Celery
        task = generate_sales_report.delay(restaurant_id, status)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)
    

class CheckReportStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        response_data = {
            "task_id": task_id,
            "status": task_result.status,
            "result": task_result.result if task_result.ready() else None
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
class DownloadReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, filename):
        filepath = os.path.join('reports', filename)
        if os.path.exists(filepath):
            response = FileResponse(open(filepath, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
        return HttpResponseNotFound("File not found")