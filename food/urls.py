from django.conf.urls import url, include
from django.urls import path

from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^search/$', views.search, name='search'),
    url(r'^(?P<food_id>\d+)/$', views.show, name='show'),
    url(r'^(?P<food_id>\d+)/save_product', views.save_product, name='save_product'),
]
