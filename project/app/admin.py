from django.contrib import admin
from .models import Product, FAQ, Category

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(FAQ)

