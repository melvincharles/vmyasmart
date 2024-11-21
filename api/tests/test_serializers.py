from django.test import TestCase
from api.serializers import CategorySerializer
from shop.models import Catagory

class CategorySerializerTest(TestCase):
    def setUp(self):
        self.category = Catagory.objects.create(
            name="Books",
            description="All types of books",
            status=True
        )
        self.serializer = CategorySerializer(instance=self.category)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(data['name'], "Books")
        self.assertEqual(data['description'], "All types of books")
        self.assertTrue(data['status'])
