from django.contrib import admin
from .models import Product, ProductType, Category, Tag

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(Category)
admin.site.register(Tag)