from django.contrib import admin
from . import models

#=============================================================================
# Session 59,60 __  __  :

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title', 'id', 'price', 'is_active']
# list_filter = [] ---> to filter items based on which attrs are in this list
    list_filter = ['price', 'category']
    list_editable = ['price', 'is_active']
    ordering = ['id']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)
