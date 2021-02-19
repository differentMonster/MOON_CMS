from django.db import models
from django.conf import settings
from django_countries.fields import CountryField

# Create your options here.
# Address
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class ProductModel(models.Model):
    product_name = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    origianl_url = models.TextField()
    image_url = models.TextField()
    quality = models.PositiveIntegerField(default=1)

    def __self__(self):
        return self.product_name

# Address database
class AddressModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    country = CountryField(multiple=False)
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.street_address1

    class Meta:
        verbose_name_plural = 'Addresses'

# Create your models here.
# Cart datatbase - Shopping cart
class CartModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField(ProductModel)
    shipping_address = models.ForeignKey(
        'AddressModel', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'AddressModel', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)

    def __self__(self):
        return self.user

# Order Model
class OrderModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey('CartModel', on_delete=models.CASCADE, blank=True, null=True)
    items = models.ManyToManyField(ProductModel)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")

class UserAccountModel(models.Model):
    pass
