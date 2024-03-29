from django.contrib import admin

# Register your models here.
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["sku", "name", "category", "price", "rating", "image"]
    ordering = ["-sku"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["friendly_name", "name"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
