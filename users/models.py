from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    TYPOLOGY_CHOICES = [
        ('distribuidor', 'Distribuidor'),
        ('cliente', 'Cliente'),
    ]
    typology = models.CharField(max_length=20, choices=TYPOLOGY_CHOICES, null=True, blank=True)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    default_address = models.TextField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",  # Cambia esto a un nombre único
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",  # Cambia esto a un nombre único
        related_query_name="user",
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'