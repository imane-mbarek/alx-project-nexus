from django.contrib import admin
from .models import Product, CartItem
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('user__username', 'product__name')  # Allow search by username and product name
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
