from django.contrib import admin

from . import models

# from django.contrib.auth.models import User
from .models import User


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]


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


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user", "location"]
    list_display = [
        "payrol",
        "location",
        "first_name",
        "last_name",
        "email",
    ]


@admin.register(models.Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = [
        "placed_at",
        "staff",
        "location_from",
        "location_to",
        "delivery_no",
        "in_transit",
    ]
    list_per_page = 20
    list_filter = [
        "location_to",
        "staff",
        "location_from",
    ]
    list_editable = [
        "in_transit",
    ]


@admin.register(models.DeliveryAssets)
class DeliveryAssetsAdmin(admin.ModelAdmin):
    list_display = (
        "delivery",
        "asset",
        "quantity",
        "received",
    )
    list_select_related = ["asset", "delivery"]
    # search_fields = [
    #     "delivery",
    #     "asset",
    # ]
    list_editable = [
        "received",
    ]
