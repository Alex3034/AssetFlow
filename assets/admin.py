from django.contrib import admin
from assets.models import Category, Product, StockMovement, Supplier

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'supplier', 'price', 'stock_quantity', 'is_low_stock', 'created_at')
    list_filter = ('category', 'supplier', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone', 'address', 'created_at')
    search_fields = ('name', 'contact_email')
    ordering = ('name',)

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity', 'user', 'created_at')
    list_filter = ('movement_type', 'created_at')
    search_fields = ('product__name', 'reason')
    ordering = ('-created_at',)
