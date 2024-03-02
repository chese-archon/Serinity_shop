from django.contrib import admin
from .models import Product#, ProductImage
# Register your models here.

admin.site.register(Product)
#admin.site.register(ProductImage)
#@admin.register(Product)
#class ProductAdmin(admin.ModelAdmin):
#    list_display = ['name', 'price', 'height', 'width', 'depth']  # Определение отображаемых полей

# Регистрация модели ProductImage в административной панели
#@admin.register(ProductImage)
#class ProductImageAdmin(admin.ModelAdmin):
#    list_display = ['product', 'image']  # Определение отображаемых полей