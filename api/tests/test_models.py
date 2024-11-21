from django.test import TestCase
from shop.models import Catagory, Product

class CatagoryModelTest(TestCase):
    def setUp(self):
        self.category = Catagory.objects.create(
            name="Electronics",
            description="All electronic items",
            status=True
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
        self.assertEqual(self.category.description, "All electronic items")
        self.assertTrue(self.category.status)
