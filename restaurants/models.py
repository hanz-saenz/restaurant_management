from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=180, null=True, blank=True)
    latitude = models.DecimalField(max_digits=21, decimal_places=11, null=True, blank=True)
    longitude = models.DecimalField(max_digits=21, decimal_places=11, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'
        ordering = ['name']