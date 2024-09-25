from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.IntegerField(max_length=50, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
    #def __len__(self):
    #    return int(self.price)