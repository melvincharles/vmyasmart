# from atexit import register
# from django.contrib import admin
# from .models import *



# admin.site.register(Catagory)
# admin.site.register(Product)
# admin.site.register(Cart)
# admin.site.register(Favourite)
from django.contrib import admin
from .models import Catagory, Product, Cart, Favourite, FeatureProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'original_price', 'selling_price', 'quantity', 'trending', 'status')
    list_editable = ('trending', 'status') 
    list_filter = ('category', 'trending', 'status') 
    search_fields = ('name', 'vendor') 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_products')  
    search_fields = ('name',) 

    def total_products(self, obj):
       
        return obj.product_set.count() 

    total_products.short_description = 'Total Products'  

class FeatureProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'vendor', 'is_featured')  
    list_filter = ('category', 'is_featured') 
    search_fields = ('name', 'vendor') 

admin.site.register(Catagory, CategoryAdmin)  
admin.site.register(Product, ProductAdmin)
admin.site.register(FeatureProduct, FeatureProductAdmin) 
admin.site.register(Cart)
admin.site.register(Favourite)
