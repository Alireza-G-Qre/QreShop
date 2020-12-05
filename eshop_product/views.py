from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *


# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.get_active_product()


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    def get_queryset(self):
        return Product.objects.get_active_product();
