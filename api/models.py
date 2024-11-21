from django.db import models
from shop.models import Category 
from shop.models import FeatureProduct

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    vendor = models.CharField(max_length=150)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)
    quantity = models.IntegerField()
    original_price = models.FloatField()
    selling_price = models.FloatField()
    description = models.TextField()
    status = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    is_featured = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
