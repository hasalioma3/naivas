# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser
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
    barcode = models.CharField(max_length=10)
    serial_no = models.CharField(max_length=225)
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


class Delivery(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    location_from = models.ForeignKey(Location, on_delete=models.PROTECT,related_name="deliveries_from")
    location_to = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="deliveries_to")
    delivery_no = models.CharField(max_length=225, unique=True)
