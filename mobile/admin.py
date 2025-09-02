from django.contrib import admin
from .models import Category
from .models import Products


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("id","name","description","icon")


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=("id","name","brand","price","category","storge","color")
