from django.conf.urls import url, include
from django.urls import path

from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'products/', views.products),
    url(r'^better/(?P<food_id>\d+)/$', views.better, name='better'),
    url(r'^better/(?P<food_id>\d+)/save_product', views.save_product, name='save_product'),
]
