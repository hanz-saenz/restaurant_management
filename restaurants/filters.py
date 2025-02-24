import django_filters
from .models import Restaurant

class RestaurantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por nombre (búsqueda insensible a mayúsculas)
    category = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por categoría
    status = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por estado
    min_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')  # Filtro por rating mínimo
    max_rating = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')  # Filtro por rating máximo
    active = django_filters.BooleanFilter()  # Filtro por estado activo/inactivo

    class Meta:
        model = Restaurant
        fields = ['name', 'category', 'status', 'min_rating', 'max_rating', 'active']