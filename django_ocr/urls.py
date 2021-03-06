"""django_ocr URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from food import views as food

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', food.index, name='food'),
    path('food/', include('food.urls')),
    path('search/', include('search.urls')),
    path('favorite/', include('favorite.urls')),
    path('my_profile/', include('my_profile.urls')),
    path('legal/', include('legal.urls')),
    path('sign_up/', include('sign_up.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
