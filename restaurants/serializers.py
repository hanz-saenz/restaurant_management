from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        # fields = [
        #     'id', 'name', 'address', 'rating', 'status', 'category',
        #     'latitude', 'longitude', 'created_at', 'updated_at', 'active'
        # ]