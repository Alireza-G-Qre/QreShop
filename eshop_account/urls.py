from django.urls import path
from .views import *

app_name = 'eshop_account'

urlpatterns = [
    path('account_login', account_login, name='account_login'),
    path('account_register', account_register, name='account_register'),
    path('account_logout', account_logout, name='account_logout'),
]
