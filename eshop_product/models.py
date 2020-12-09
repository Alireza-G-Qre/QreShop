from django.db import models
from random import randint
from os import path
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.


class ProductManager(models.Manager):
    def get_active_product(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):
        return self.get_queryset().filter(id=product_id).first()


def upload_image_path(instance, address):
    code = randint(1000000, 10000000)
    name = path.basename(address)
    name, e = path.splitext(name)
    return f'{name + (10 - len(name)) * "-"}-{code}{e}'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(null=True, blank=True, upload_to=upload_image_path, verbose_name='تصویر')
    active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True, editable=False)

    objects = ProductManager()

    def get_absolute_url(self):
        return f"/product_detail/{self.slug}"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
