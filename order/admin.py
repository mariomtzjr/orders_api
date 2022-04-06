from django.contrib import admin

from order.models import Order, OrderItem

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title', 'grand_total', 'is_paid', 'ordered_at', 'order_items']
    list_filter = ['title', 'grand_total', 'is_paid', 'ordered_at']
    search_fields = ['title']
    list_per_page = 50
    fields = ['title', 'grand_total', 'order_items', 'is_paid', 'ordered_at']