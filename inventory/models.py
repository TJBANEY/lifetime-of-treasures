from django.db import models
from filebrowser.fields import FileBrowseField

class Category(models.Model):
    name = models.CharField(max_length=255)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    description = models.TextField(max_length=700, default="")
    image = FileBrowseField(max_length=300, directory="media/inventory/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"
