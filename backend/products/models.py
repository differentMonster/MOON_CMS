from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
# Upload_storage = FileSystemStorage(location='/core/static')

#+descption: upload image block POST request

# Create your models here.
class CheongsamModel(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(max_length=200, blank=True, default="default.png")
    photo2 = models.ImageField(max_length=200, blank=True, default="default2.png")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

def __self__(self):
    return self.name

# Create your models here.
class TeasetModel(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(max_length=200, blank=True, default="default.png")
    photo2 = models.ImageField(max_length=200, blank=True, default="default2.png")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

def __self__(self):
    return self.name
