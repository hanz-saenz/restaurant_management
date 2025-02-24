from rest_framework import serializers
from .models import Order, Origin
from menu.serializers import MenuItemSerializer

class OriginSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)  # Serializa el ítem del menú asociado

    class Meta:
        model = Origin
        fields = ['id', 'menu_item', 'quantity', 'subtotal', 'notes']

class OrderSerializer(serializers.ModelSerializer):
    origins = OriginSerializer(many=True, read_only=True)  # Serializa los orígenes asociados

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'updated_at', 'active', 'origins']