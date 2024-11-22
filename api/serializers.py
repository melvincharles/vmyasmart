from rest_framework import serializers
from shop.models import Catagory

class CategorySerializer(serializers.ModelSerializer):  # You can still use "Category" for consistency
    class Meta:
        model = Catagory  # Ensure this matches the model name
        fields = ["id", "name", "image", "description", "status", "created_at"]

from rest_framework import serializers
from shop.models import Product, Catagory

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Catagory.objects.all(),
        slug_field='name'  
    )

    class Meta:
        model = Product
        fields = [
            "id", "name", "vendor", "product_image", "quantity",
            "original_price", "selling_price", "description", "status",
            "trending", "is_featured", "category"
        ]


from rest_framework import serializers
from shop.models import FeatureProduct

class FeatureProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureProduct
        fields = ['id', 'name', 'vendor', 'product_image', 'category', 'is_featured']
