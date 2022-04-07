from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name}"
