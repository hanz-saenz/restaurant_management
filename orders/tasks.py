import csv
import os
from celery import shared_task
from django.utils import timezone
from restaurants.models import Restaurant
from orders.models import Order, Origin
from datetime import datetime

@shared_task
def generate_sales_report(restaurant_id, month):
    # Obtener el restaurante
    restaurant = Restaurant.objects.get(id=restaurant_id)
    
    # Filtrar órdenes por mes
    orders = Order.objects.filter(
        user__restaurant=restaurant,
        created_at__month=month
    )
    
    # Calcular total de ventas y precio total
    total_sales = orders.count()
    total_price = sum(
        origin.subtotal for order in orders for origin in order.origins.all()
    )
    
    # Crear el archivo CSV
    filename = f"sales_report_{restaurant_id}_{month}.csv"
    filepath = os.path.join('reports', filename)
    
    os.makedirs('reports', exist_ok=True)  # Crear la carpeta si no existe
    
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Nombre', 'Total de Ventas', 'Total Precio Ventas'])
        writer.writerow([restaurant.id, restaurant.name, total_sales, total_price])
    
    return filename