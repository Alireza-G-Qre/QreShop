from django.db import models
from random import randint
from os import path
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.


class ProductManager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)


def upload_image_path(instance, address):
    code = randint(1000000, 10000000)
    name = path.basename(address)
    name, e = path.splitext(name)
    return f'{name + (10 - len(name)) * "-"}-{code}{e}'


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to=upload_image_path)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()
    slug = models.SlugField(blank=True, unique=True)


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
