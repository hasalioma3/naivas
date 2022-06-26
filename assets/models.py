# Create your models here.
import re

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]


class Location(models.Model):
    location_id = models.IntegerField()
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["location_id"]


class Asset(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    is_consumable = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="assets"
    )
    barcode = models.CharField(max_length=10, unique=True)
    serial_no = models.CharField(max_length=225, unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["created_on"]


class Staff(models.Model):
    payrol = models.CharField(max_length=225, unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ["user__first_name", "user__last_name"]

    @admin.display(ordering="user__last_name")
    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email


class Delivery(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    location_from = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="deliveries_from"
    )
    location_to = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="deliveries_to"
    )
    delivery_no = models.CharField(max_length=225, unique=True)
    in_transit = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.delivery_no

    class Meta:
        ordering = [
            "delivery_no",
        ]


class DeliveryAssets(models.Model):
    delivery = models.ForeignKey(
        Delivery, on_delete=models.PROTECT, related_name="assets"
    )
    asset = models.ForeignKey(
        Asset, on_delete=models.PROTECT, related_name="deliveryassets"
    )
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    received = models.BooleanField(default=False)

    class Meta:
        unique_together = [
            "delivery",
            "asset",
        ]
