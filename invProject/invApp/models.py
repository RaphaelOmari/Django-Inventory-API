from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Use this if you want to explicitly define product_id as the PK
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    @property
    def stock_status(self):
        return 'in_stock' if self.quantity > 0 else 'out_of_stock'
    
    def __str__(self):
        return self.name
