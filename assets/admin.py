from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]


@admin.register(models.Asset)
class AssetAdmin(admin.ModelAdmin):
    autocomplete_fields = ["location"]
    prepopulated_fields = {"slug": ["title"]}
    list_display = [
        "title",
        "barcode",
        "serial_no",
        "location",
        "is_consumable",
        "created_on",
        "last_update",
        "category_title",
    ]
    list_editable = [
        "location",
    ]
    list_per_page = 20
    list_filter = ["category", "location"]
    list_select_related = ["category", "location"]
    search_fields = [
        "title",
        "barcode",
        "serial_no",
        "location",
    ]

    def category_title(self, asset: models.Asset):
        return asset.category.title
