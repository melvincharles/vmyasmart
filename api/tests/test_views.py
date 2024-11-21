from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from shop.models import Catagory

class CategoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Catagory.objects.create(
            name="Fashion",
            description="Clothing and accessories",
            status=True
        )

    def test_get_categories(self):
        response = self.client.get(reverse('category-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
