from django.contrib import admin

from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'quantity', 'unit_price']
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 50
    fields = ['name', 'quantity', 'unit_price',]