from django.db import models
import random
import string

def generate_product_id():
    return "".join(random.choices(string.ascii_letters + "0123456789", k=10))

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    # Basic Information
    product_id = models.CharField(
        max_length=10,
        unique=True,
        default=generate_product_id,
        editable=False,
        primary_key=True,
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    sku = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100, null=True, blank=True)
    model_number = models.CharField(max_length=100, null=True, blank=True)

    # Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    # Stock and Availability
    stock_quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    availability_status = models.CharField(max_length=50, null=True, blank=True)

    # Category and Tags
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    # Media
    image_1 = models.ImageField(
        upload_to="product_images/", default="product_images/default.jpg"
    )
    image_2 = models.ImageField(
        upload_to="product_images/",
        default="product_images/default.jpg",
        null=True,
        blank=True,
    )
    image_3 = models.ImageField(
        upload_to="product_images/",
        default="product_images/default.jpg",
        null=True,
        blank=True,
    )
    image_4 = models.ImageField(
        upload_to="product_images/",
        default="product_images/default.jpg",
        null=True,
        blank=True,
    )
    image_5 = models.ImageField(
        upload_to="product_images/",
        default="product_images/default.jpg",
        null=True,
        blank=True,
    )

    # Dates
    date_added = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    # Additional Information
    weight = models.FloatField(null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    material = models.CharField(max_length=100, null=True, blank=True)
    warranty_period = models.CharField(max_length=50, null=True, blank=True)
    power_consumption = models.CharField(max_length=50, null=True, blank=True)
    battery_life = models.CharField(max_length=50, null=True, blank=True)
    specifications = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name