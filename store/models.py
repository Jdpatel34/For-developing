from django.db import models
from django.db import models
from store.common.constants import ProductTypes, BrandTypes, QualityType

# Create your models here.
class LoginUser(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=15, default='United Kindom')
    state = models.CharField(max_length=15)
    postcode = models.CharField(max_length=10)

    def get_username(self) -> str:
        return self.username


class Products(models.Model):
    name = models.CharField(max_length=50)
    descreption = models.TextField(max_length=200)
    product_type = models.IntegerField(choices=ProductTypes.choices)
    brand_type = models.IntegerField(choices=BrandTypes.choices)


class ProductDetails(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_details')
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=100)
    qr_code = models.IntegerField(null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    price = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    quality_type = models.IntegerField(choices=QualityType.choices, default=QualityType.COPY)
    description = models.CharField(max_length=400)


class Brand(models.Model):
    name = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)
