# Generated by Django 3.1.2 on 2020-12-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product', '0008_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]
