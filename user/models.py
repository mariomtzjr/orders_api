from django.db import models


# Create your models here.
class Operator(models.Model):
    employee_number = models.PositiveBigIntegerField(default=0)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Operators'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comensal(models.Model):
    table_number = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Comensales'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - Mesa: {self.table_number}"