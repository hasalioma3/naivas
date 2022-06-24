from django.db import models

# Create your models here.


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
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    payrol = models.CharField(max_length=225, unique=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name", "last_name"]
