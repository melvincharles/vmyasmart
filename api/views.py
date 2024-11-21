from shop.models import Product, Catagory
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.generics import ListCreateAPIView

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListCreateView(ListCreateAPIView):
    queryset = Catagory.objects.all()  # Use the correct model name
    serializer_class = CategorySerializer

from rest_framework import generics
from shop.models import FeatureProduct
from .serializers import FeatureProductSerializer

class FeatureProductListView(generics.ListCreateAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

