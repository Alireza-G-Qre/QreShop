"""QreShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('Header/', BehindHeader.as_view(), name='Header'),
    path('Footer/', BehindFooter.as_view(), name='Footer'),
    path('HomePage/', home_page, name='HomePage'),
    path('', redirect_home, name='goHome'),
    path('', include('eshop_account.urls', namespace='account')),
    path('', include('eshop_product.urls', namespace='product')),
    path('admin/', admin.site.urls),
]

from django.conf.urls.static import static
from QreShop import settings

if settings.DEBUG:
    # add root static files
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
