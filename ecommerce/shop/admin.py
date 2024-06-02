# shop/admin.py

from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
