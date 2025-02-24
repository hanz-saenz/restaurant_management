import django_filters
from .models import MenuItem

class MenuItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por nombre (búsqueda insensible a mayúsculas)
    category = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por categoría
    available = django_filters.BooleanFilter()  # Filtro por disponibilidad
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')  # Filtro por precio mínimo
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')  # Filtro por precio máximo

    class Meta:
        model = MenuItem
        fields = ['restaurant', 'name', 'category', 'available', 'min_price', 'max_price']