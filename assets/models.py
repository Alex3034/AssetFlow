from django.conf import settings
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)

    category = models.ForeignKey(
        'Category', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='products'
    )
    supplier = models.ForeignKey(
        'Supplier', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='products'
    )

    stock_quantity = models.PositiveIntegerField(default=0)
    minimum_stock = models.PositiveIntegerField(default=5)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name
    
    @property
    def is_low_stock(self):
        return self.stock_quantity <= self.minimum_stock

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=150, unique=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']

    def __str__(self):
        return self.name

class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'Entrada'),
        ('OUT', 'Salida'),
    ]

    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='movements'
    )
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.PositiveIntegerField()
    reason = models.CharField(max_length=255, blank=True)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='stock_movements'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Stock Movement'
        verbose_name_plural = 'Stock Movements'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} ({self.quantity})"