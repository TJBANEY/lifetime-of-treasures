from django.contrib import admin

from inventory.models import InventoryItem, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

@admin.register(InventoryItem)
class InventoryAdmin(admin.ModelAdmin):
    model = InventoryItem

    list_display = ('name', 'category', 'price', 'created_at')