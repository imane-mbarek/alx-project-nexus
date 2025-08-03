from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')  # Display these fields in the list view
    search_fields = ('name', 'description')  # Enable search by name or description
    list_filter = ('created_at', 'updated_at')  # Add filters for creation and update dates
    ordering = ('-created_at',)  # Order by latest created products first
