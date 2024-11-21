from django.urls import path
from .views import ProductListCreateView, CategoryListCreateView
from .views import FeatureProductListView
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/Featureproducts/', FeatureProductListView.as_view(), name='feature-products'),

]
