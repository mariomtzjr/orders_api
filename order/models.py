import datetime
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete

from product.models import Product


# Create your models here.
class Order(models.Model):
    operador = models.ForeignKey('user.Operator', on_delete=models.PROTECT)
    comensal = models.OneToOneField('user.Comensal', on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)
    title = models.CharField(blank=True, max_length=150)
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    grand_total = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=False)

    ordered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-ordered_at']
    
    def __str__(self):
        return f"Order - {self.id}"

    def save(self, *args, **kwargs):
        order_items = self.order_items.all()

        self.total = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        self.grand_total = Decimal(self.total) - Decimal(self.discount)
        self.title = f"Order: {self.id}"
        super().save(*args, **kwargs)



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_item')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_items')
    qty = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

    def __str__(self):
        return f'{self.product.name}'

    def save(self,  *args, **kwargs):
        print("Saving OrderItem")

        self.unit_price = Product.objects.get(id=self.product.id).unit_price
        self.final_price = self.discount_price if self.discount_price > 0 else self.unit_price
        self.total_price = Decimal(self.qty) * Decimal(self.final_price)
        super().save(*args, **kwargs)
        self.order.save()


@receiver(post_delete, sender=OrderItem)
def delete_order_item(sender, instance, **kwargs):
    """The first signal occurs when we delete a order,
    so we tell to the system before you delete the order find all order items and delete them.
    
    The second signal occurs we delete a order item,
    just before the delete we return the qty to warehouse.

    Args:
        sender (object): order_item instance
        instance (object): order_item instance
    """
    product = instance.product
    product.quantity += instance.quantity
    product.save()
    instance.order.save()