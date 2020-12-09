from .views import *
from django.urls import path

app_name = 'eshop_product'

urlpatterns = [
    path('product_list', ProductList.as_view(), name='product_list'),
    path('product_detail/<slug>', ProductDetail.as_view(), name='product_detail'),
    path('products/search', SearchProductsView.as_view()),
]
