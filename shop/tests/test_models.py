from django.test import TestCase
from .models import Product, Catagory

class ProductModelTest(TestCase):
    def setUp(self):
        category = Catagory.objects.create(name="Electronics")
        Product.objects.create(
            category=category,
            name="Phone",
            vendor="VendorA",
            original_price=500,
            selling_price=400,
            quantity=10
        )

    def test_product_creation(self):
        product = Product.objects.get(name="Phone")
        self.assertEqual(product.selling_price, 400)
