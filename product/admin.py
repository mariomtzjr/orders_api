from django.contrib import admin

from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_price']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 50
    fields = ['name', 'quantity', 'unit_price', 'created_at', 'updated_at',]
    readonly_fields = ['created_at', 'updated_at', 'quantity']