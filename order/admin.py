from django.contrib import admin

from order.models import Order, OrderItem

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'grand_total', 'is_paid']
    list_filter = ['title', 'grand_total', 'is_paid', 'ordered_at']
    search_fields = ['title']
    fields = ['title', 'grand_total', 'is_paid']
    readonly_fields = ['ordered_at', 'updated_at']