import django_filters
from .models import User

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por nombre (búsqueda insensible a mayúsculas)
    last_name = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por apellido
    email = django_filters.CharFilter(lookup_expr='icontains')  # Filtro por correo electrónico
    typology = django_filters.CharFilter(lookup_expr='exact')  # Filtro por tipología (dealer, customer)
    restaurant = django_filters.NumberFilter(field_name='restaurant__id')  # Filtro por ID del restaurante
    active = django_filters.BooleanFilter()  # Filtro por estado activo/inactivo

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'typology', 'restaurant', 'active']